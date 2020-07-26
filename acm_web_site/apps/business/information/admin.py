from django.contrib import admin

from utils.utils import upload_file

from .models import *
from .forms import (
    AwardAdminForm,
)


# TODO - Put picture path logic in Utils

# Register your models here.
class AwardAdmin(admin.ModelAdmin):
    form = AwardAdminForm

    def save_model(self, request, obj, form, change):
        obj.picture = upload_file(request, 'picture')
        super().save_model(request, obj, form, change)


admin.site.register(Award, AwardAdmin)
