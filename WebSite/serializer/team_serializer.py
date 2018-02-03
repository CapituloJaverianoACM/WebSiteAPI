# -- coding: utf-8
from __future__ import unicode_literals

from rest_framework import serializers

from WebSite.serializer.member_serializer import MemberSerializer


class TeamSerializer(serializers.Serializer):
    name = serializers.CharField()
    picture = serializers.ImageField()
    members = MemberSerializer(many=True)
