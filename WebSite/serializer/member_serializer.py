from rest_framework import serializers
from WebSite.models import (
    Member,
    POSITION_CHOICES,
    MAJOR_CHOICES
)


class MemberSerializer(serializers.Serializer):
    name = serializers.CharField()
    surname = serializers.CharField()
    email = serializers.CharField()
    major = serializers.ChoiceField(
        choices=MAJOR_CHOICES
    )
    identification = serializers.CharField(required=False)
    date_major = serializers.DateField(required=False)
    date_chapter = serializers.DateField(required=False)
    date_birth = serializers.DateField(required=False)
    cellphone = serializers.CharField(required=False)
    is_staff = serializers.BooleanField(default=False)
    position = serializers.ChoiceField(
        choices=POSITION_CHOICES,
        required=False
    )
    description = serializers.CharField(required=False)

    def create(self, validated_data):
        return Member.objects.create(**validated_data)
