# -- coding: utf-8
from __future__ import unicode_literals
import base64

from rest_framework import serializers

from acm_web_site.settings import MEDIA_ROOT
from web_site.models import Team


class TeamSerializer(serializers.ModelSerializer):
    picture = serializers.SerializerMethodField(required=False)

    class Meta:
        model = Team
        fields = '__all__'

    def get_picture(self, obj):
        prefix = '/'.join(MEDIA_ROOT.split('/')[:-1])
        complete_path = prefix + obj.picture
        with open(complete_path, "rb") as image_file:
            str = base64.b64encode(image_file.read())
        return str
