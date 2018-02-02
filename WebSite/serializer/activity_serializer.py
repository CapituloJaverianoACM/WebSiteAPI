# -- coding: utf-8
from __future__ import unicode_literals

from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from rest_framework import serializers

from WebSite.models import Member


class ActivitySerializer(serializers.Serializer):
    name = serializers.CharField()
    date = serializers.DateTimeField()
    place = serializers.CharField()
    # TODO lack relations many to many


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
