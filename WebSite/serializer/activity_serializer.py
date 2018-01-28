# -- coding: utf-8
from __future__ import unicode_literals

from rest_framework import serializers


class ActivitySerializer(serializers.Serializer):
    name = serializers.CharField()
    date = serializers.DateTimeField()
    place = serializers.CharField()
    # TODO lack relations many to many
