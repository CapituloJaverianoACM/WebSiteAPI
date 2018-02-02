# -- coding: utf-8
from __future__ import unicode_literals

from rest_framework import serializers


class AwardSerializer(serializers.Serializer):
    date = serializers.CharField()
    description = serializers.CharField()
    title = serializers.CharField()
    picture = serializers.ImageField()
