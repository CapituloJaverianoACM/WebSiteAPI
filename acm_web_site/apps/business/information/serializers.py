from django.conf import settings
from utils.utils import encode_media
from rest_framework import serializers
from .models import (
    Award,
)

import base64


class AwardSerializer(serializers.ModelSerializer):
    picture = serializers.SerializerMethodField('get_picture')

    class Meta:
        model = Award
        fields = '__all__'

    def get_picture(self, obj):
        return encode_media(obj.picture)
