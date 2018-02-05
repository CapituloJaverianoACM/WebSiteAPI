from django import forms

from django.contrib.admin.widgets import AdminDateWidget

from WebSite.models import Activity
from WebSite.models import Member
from WebSite.models import Project
from WebSite.models import Team
from WebSite.models import Tutorial


class GalleryAdminForm(forms.ModelForm):
    picture = forms.FileField()


class AwardAdminForm(forms.ModelForm):
    date = forms.DateField(widget=AdminDateWidget())
    picture = forms.FileField()
    description = forms.CharField()
    title = forms.CharField()


class ActivityAdminForm(forms.ModelForm):
    poster = forms.FileField()

    class Meta:
        model = Activity
        fields = '__all__'


class MemberAdminForm(forms.ModelForm):
    picture = forms.FileField()

    class Meta:
        model = Member
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
