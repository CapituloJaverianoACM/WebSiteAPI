# -- coding: utf-8
from __future__ import unicode_literals
import base64

from django.conf import settings
from rest_framework import serializers
from WebSite.models import Award

MEDIA_ROOT = getattr(settings, "MEDIA_ROOT", None)

class AwardSerializer(serializers.ModelSerializer):
    picture = serializers.SerializerMethodField()

    class Meta:
        model = Award
        fields = '__all__'

    def get_picture(self, obj):
        prefix = '/'.join(MEDIA_ROOT.split('/')[:-1])
        complete_path = prefix + obj.picture
        with open(complete_path, "rb") as image_file:
            str = base64.b64encode(image_file.read())
        return str
