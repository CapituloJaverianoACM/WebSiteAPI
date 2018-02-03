from django import forms

from django.contrib.admin.widgets import AdminDateWidget

class FileAdminForm(forms.ModelForm):
    EXT_CHOICES = (
        ('img', 'Image'),
        ('md', 'Markdown'),
        ('mdf', 'MarkdownForm'),
        ('json', 'JSON'),
        ('ot', 'Other'),
    )
    basename = forms.CharField()
    path = forms.FileField()
    ext = forms.ChoiceField(choices=EXT_CHOICES)


class AwardAdminForm(forms.ModelForm):
    date = forms.DateField(widget=AdminDateWidget())
    picture = forms.FileField()
    description = forms.CharField()
    title = forms.CharField()