# -- coding: utf-8
from __future__ import unicode_literals
import base64
import pytz
from datetime import datetime

from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from rest_framework import serializers

from django.conf import settings
from WebSite.models import Member
from WebSite.models import Activity

MEDIA_ROOT = getattr(settings, "MEDIA_ROOT", None)


class ActivitySerializer(serializers.ModelSerializer):
    poster = serializers.SerializerMethodField()
    show_form = serializers.SerializerMethodField()

    class Meta:
        model = Activity
        fields = '__all__'

    def get_poster(self, obj):
        prefix = '/'.join(MEDIA_ROOT.split('/')[:-1])
        complete_path = prefix + obj.poster
        with open(complete_path, "rb") as image_file:
            str = base64.b64encode(image_file.read())
        return str

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
