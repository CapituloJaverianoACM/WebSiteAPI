from django.contrib import admin

from django.core.files.storage import FileSystemStorage

from .forms import (
    ActivityAdminForm,
    TutorialAdminForm,
    ProjectAdminForm
)

from .models import (
    Activity,
    Tutorial,
    Project
)

# Register your models here.


class ActivityAdmin(admin.ModelAdmin):
    form = ActivityAdminForm

    def save_model(self, request, obj, form, change):
        file_form = request.FILES['poster']
        fs = FileSystemStorage()
        filename = fs.save(file_form.name, file_form)
        uploaded_file_url = fs.url(filename)
        obj.poster = uploaded_file_url
        super().save_model(request, obj, form, change)


class ProjectAdmin(admin.ModelAdmin):
    form = ProjectAdminForm

    def save_model(self, request, obj, form, change):
        file_form = request.FILES['poster']
        fs = FileSystemStorage()
        filename = fs.save(file_form.name, file_form)
        uploaded_file_url = fs.url(filename)
        obj.poster = uploaded_file_url
        super().save_model(request, obj, form, change)


class TutorialAdmin(admin.ModelAdmin):
    form = TutorialAdminForm

    def save_model(self, request, obj, form, change):
        file_form = request.FILES['poster']
        fs = FileSystemStorage()
        filename = fs.save(file_form.name, file_form)
        uploaded_file_url = fs.url(filename)
        obj.poster = uploaded_file_url
        super().save_model(request, obj, form, change)


admin.site.register(Tutorial, TutorialAdmin)
admin.site.register(Activity, ActivityAdmin)
admin.site.register(Project, ProjectAdmin)
