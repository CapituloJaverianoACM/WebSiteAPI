from django import forms

from .models import Member, Team


class MemberAdminForm(forms.ModelForm):
    picture = forms.FileField()

    class Meta:
        model = Member
        fields = '__all__'


class TeamAdminForm(forms.ModelForm):
    picture = forms.FileField()

    class Meta:
        model = Team
        fields = '__all__'
