# -- coding: utf-8
from __future__ import unicode_literals
import base64

from ACMWebSite.settings import MEDIA_ROOT
from rest_framework import serializers


class AwardSerializer(serializers.Serializer):
    date = serializers.CharField()
    description = serializers.CharField()
    title = serializers.CharField()
    picture = serializers.SerializerMethodField()

    def get_picture(self, obj):
        prefix = '/'.join(MEDIA_ROOT.split('/')[:-1])
        complete_path = prefix + obj.picture
        with open(complete_path, "rb") as imageFile:
            str = base64.b64encode(imageFile.read())
        return str
