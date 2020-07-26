from django.contrib import admin

from utils.utils import upload_file
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
        obj.poster = upload_file(request, 'poster')
        super().save_model(request, obj, form, change)


class ProjectAdmin(admin.ModelAdmin):
    form = ProjectAdminForm

    def save_model(self, request, obj, form, change):
        obj.poster = upload_file(request, 'poster')
        super().save_model(request, obj, form, change)


class TutorialAdmin(admin.ModelAdmin):
    form = TutorialAdminForm

    def save_model(self, request, obj, form, change):
        obj.poster = upload_file(request, 'poster')
        super().save_model(request, obj, form, change)


admin.site.register(Tutorial, TutorialAdmin)
admin.site.register(Activity, ActivityAdmin)
admin.site.register(Project, ProjectAdmin)
