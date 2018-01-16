from django import forms


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
