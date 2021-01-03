from django.contrib import admin

from utils.utils import upload_file, BaseInlineMixin
from .forms import (
    ActivityAdminForm,
    TutorialAdminForm,
    ProjectAdminForm, GalleryAdminForm
)

from .models import (
    Activity,
    Tutorial,
    Project, ActivityMember, Gallery
)

# Register your models here.


class ActivityMemberInline(admin.TabularInline):
    model = ActivityMember


class GalleryAdmin(admin.ModelAdmin):
    form = GalleryAdminForm
    def save_model(self, request, obj, form, change):
        obj.picture = upload_file(request, 'picture')
        super().save_model(request, obj, form, change)


class ActivityAdmin(admin.ModelAdmin):
    inlines = [ActivityMemberInline]
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
admin.site.register(Gallery, GalleryAdmin)
