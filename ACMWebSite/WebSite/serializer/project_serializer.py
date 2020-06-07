# -- coding: utf-8
from __future__ import unicode_literals
import base64

from rest_framework import serializers
from WebSite.models import Project
from django.conf import settings
MEDIA_ROOT = getattr(settings, "MEDIA_ROOT", None)


class ProjectSerializer(serializers.ModelSerializer):
    poster = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = '__all__'

    def get_poster(self, obj):
        prefix = '/'.join(MEDIA_ROOT.split('/')[:-1])
        complete_path = prefix + obj.poster
        with open(complete_path, "rb") as image_file:
            str = base64.b64encode(image_file.read())
        return str
