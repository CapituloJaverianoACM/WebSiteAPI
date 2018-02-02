# -- coding: utf-8
from __future__ import unicode_literals

from rest_framework import serializers


class ProjectSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    name = serializers.CharField()
    date_start = serializers.DateField()
    date_end = serializers.DateField()
    # TODO lack relations many to many
