from django.conf import settings
from ...utils import utils
from rest_framework import serializers
from .models import (
    Award,
)

import base64


# TODO - Move auxiliary functions in serializers to Utils
class AwardSerializer(serializers.ModelSerializer):
    picture = serializers.SerializerMethodField('get_picture')

    class Meta:
        model = Award
        fields = '__all__'

    def get_picture(self, obj):
        return utils.get_picture(self, obj)
