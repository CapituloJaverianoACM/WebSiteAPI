from __future__ import unicode_literals
import base64
from abc import ABCMeta

import pytz
from datetime import datetime

from django.conf import settings
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from rest_framework import serializers
from utils.utils import encode_media
from .models import POSITION_CHOICES

from .models import (
    Activity,
    Member,
    Project,
    Tutorial
)


class ActivitySerializer(serializers.ModelSerializer):
    poster = serializers.SerializerMethodField()
    show_form = serializers.SerializerMethodField()

    class Meta:
        model = Activity
        fields = '__all__'

    def get_poster(self, obj):
        return encode_media(obj.poster)

    def get_show_form(self, obj):
        show_form = True
        if isinstance(obj, Activity):
            date_now = datetime.now()
            date_now = date_now.replace(
                hour=1,
                tzinfo=pytz.timezone("America/Bogota")
            )
            date_activity = obj.date
            date_activity = date_activity.replace(
                hour=1,
                tzinfo=pytz.timezone("America/Bogota")
            )
            if date_now > date_activity:
                show_form = False
            if obj.members.count() >= obj.capacity:
                show_form = False
        return show_form


class ConfirmActivitySerializer(serializers.Serializer):
    uidb64 = serializers.CharField()
    token = serializers.CharField()

    def validate(self, data):
        uidb64 = data.get('uidb64')
        token = data.get('token')
        uid = int(urlsafe_base64_decode(uidb64))
        try:
            member = Member.objects.get(pk=uid)
            if not default_token_generator.check_token(member, token):
                raise serializers.ValidationError(
                    "The confirm activity link is no longer valid."
                )
        except Member.DoesNotExist:
            raise serializers.ValidationError(
                "The confirm activity link is no longer valid."
            )
        return data


class ProjectSerializer(serializers.ModelSerializer):
    poster = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = '__all__'

    def get_poster(self, obj):
        return encode_media(obj.poster)


class TutorialSerializer(serializers.Serializer):
    poster = serializers.SerializerMethodField('get_poster')

    class Meta:
        model = Tutorial
        fields = '__all__'

    def get_poster(self, obj):
        return encode_media(obj.poster)
