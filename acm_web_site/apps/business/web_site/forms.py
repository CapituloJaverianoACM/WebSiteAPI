from django import forms

from .models import (
    Activity,
    Award,
    Member,
    Project,
    Team,
    Tutorial
)


class GalleryAdminForm(forms.ModelForm):
    picture = forms.FileField()


class ActivityAdminForm(forms.ModelForm):
    poster = forms.FileField()

    class Meta:
        model = Activity
        fields = '__all__'


class ProjectAdminForm(forms.ModelForm):
    poster = forms.FileField()

    class Meta:
        model = Project
        fields = '__all__'


class TeamAdminForm(forms.ModelForm):
    picture = forms.FileField()

    class Meta:
        model = Team
        fields = '__all__'


class TutorialAdminForm(forms.ModelForm):
    poster = forms.FileField()

    class Meta:
        model = Tutorial
        fields = '__all__'
