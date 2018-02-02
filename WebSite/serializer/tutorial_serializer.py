# -- coding: utf-8
from __future__ import unicode_literals

from rest_framework import serializers


class TutorialSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    name = serializers.CharField()
    # TODO  lack relations many to many
