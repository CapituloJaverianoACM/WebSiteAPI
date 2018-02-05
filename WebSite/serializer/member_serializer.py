# -- coding: utf-8
from __future__ import unicode_literals
import base64

from ACMWebSite.settings import MEDIA_ROOT

from rest_framework import serializers
from WebSite.models import Member


class MemberSerializer(serializers.Serializer):
    picture = serializers.SerializerMethodField(required=False)

    class Meta:
        model = Member
        fields = '__all__'

    def get_picture(self, obj):
        prefix = '/'.join(MEDIA_ROOT.split('/')[:-1])
        complete_path = prefix + obj.picture
        with open(complete_path, "rb") as image_file:
            str = base64.b64encode(image_file.read())
        return str
