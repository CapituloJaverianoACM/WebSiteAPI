from django import forms

from .models import (
    Award,
)


class AwardAdminForm(forms.ModelForm):
    picture = forms.FileField()

    class Meta:
        model = Award
        fields = '__all__'
