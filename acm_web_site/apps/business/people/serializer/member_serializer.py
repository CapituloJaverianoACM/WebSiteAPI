# -- coding: utf-8
from __future__ import unicode_literals
import base64

from django.conf import settings

from rest_framework import serializers

from ..models import Member, POSITION_CHOICES


class MemberSerializer(serializers.ModelSerializer):
    picture = serializers.SerializerMethodField(required=False)
    position = serializers.SerializerMethodField(required=False)

    class Meta:
        model = Member
        fields = '__all__'

    def get_position(self, obj):
        if isinstance(obj, Member):
            for key in POSITION_CHOICES:
                if key[0] == obj.position:
                    display_name = key[1]
        else:
            display_name = ''
        return display_name

    def get_picture(self, obj):
        if isinstance(obj, Member):
            prefix = '/'.join(settings.MEDIA_ROOT.split('/')[:-1])
            complete_path = prefix + obj.picture
            with open(complete_path, "rb") as image_file:
                str = base64.b64encode(image_file.read())
        else:
            str = ''
        return str

    def create(self, validated_data):
        return Member.objects.create(**validated_data)
