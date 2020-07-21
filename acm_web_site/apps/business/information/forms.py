from django import forms

from .models import (
    Award,
    Member,
)


class AwardAdminForm(forms.ModelForm):
    picture = forms.FileField()

    class Meta:
        model = Award
        fields = '__all__'


class MemberAdminForm(forms.ModelForm):
    picture = forms.FileField()

    class Meta:
        model = Member
        fields = '__all__'
