from django.conf import settings

from rest_framework import serializers
from .models import (
    Award,
)

import base64


# TODO - Move auxiliary functions in serializers to Utils
class AwardSerializer(serializers.ModelSerializer):
    picture = serializers.SerializerMethodField()

    class Meta:
        model = Award
        fields = '__all__'

    def get_picture(self, obj):
        prefix = '/'.join(settings.MEDIA_ROOT.split('/')[:-1])
        complete_path = prefix + obj.picture
        with open(complete_path, "rb") as image_file:
            str = base64.b64encode(image_file.read())
        return str
