from django.conf import settings

from rest_framework import serializers
from .models import (
    Member,
    Award,
    POSITION_CHOICES
)

import base64


# TODO - Move auxiliary functions in serializers to Utils

class MemberSerializer(serializers.ModelSerializer):
    picture = serializers.SerializerMethodField(required=False)
    position = serializers.SerializerMethodField(required=False)

    class Meta:
        model = Member
        fields = '__all__'

    def get_position(self, obj):
        display_name = ''
        if isinstance(obj, Member):
            for key in POSITION_CHOICES:
                if key[0] == obj.position:
                    display_name = key[1]
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
