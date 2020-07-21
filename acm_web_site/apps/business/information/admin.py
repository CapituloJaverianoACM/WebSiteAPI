from django.contrib import admin

from django.core.files.storage import FileSystemStorage

from .models import *
from .forms import (
    AwardAdminForm,
    MemberAdminForm,
)


# Register your models here.


class AwardAdmin(admin.ModelAdmin):
    form = AwardAdminForm

    def save_model(self, request, obj, form, change):
        file_form = request.FILES['picture']
        fs = FileSystemStorage()
        filename = fs.save(file_form.name, file_form)
        uploaded_file_url = fs.url(filename)
        obj.picture = uploaded_file_url
        super().save_model(request, obj, form, change)


class MemberAdmin(admin.ModelAdmin):
    form = MemberAdminForm

    def save_model(self, request, obj, form, change):
        file_form = request.FILES['picture']
        fs = FileSystemStorage()
        filename = fs.save(file_form.name, file_form)
        uploaded_file_url = fs.url(filename)
        obj.picture = uploaded_file_url
        super().save_model(request, obj, form, change)


admin.site.register(Member, MemberAdmin)
admin.site.register(Award, AwardAdmin)
