# -- coding: utf-8
from __future__ import unicode_literals
import base64

from rest_framework import serializers

from ACMWebSite.settings import MEDIA_ROOT
from WebSite.models import Tutorial


class TutorialSerializer(serializers.Serializer):
    poster = serializers.SerializerMethodField()

    class Meta:
        model = Tutorial
        fields = '__all__'

    def get_poster(self, obj):
        prefix = '/'.join(MEDIA_ROOT.split('/')[:-1])
        complete_path = prefix + obj.picture
        with open(complete_path, "rb") as image_file:
            str = base64.b64encode(image_file.read())
        return str
