from django.contrib import admin
from utils.utils import upload_file

from .forms import MemberAdminForm, TeamAdminForm
from .models import Member, Team


class MemberAdmin(admin.ModelAdmin):
	form = MemberAdminForm

	def save_model(self, request, obj, form, change):
		obj.picture = upload_file(request, 'picture')
		super().save_model(request, obj, form, change)


class TeamAdmin(admin.ModelAdmin):
	form = TeamAdminForm

	def save_model(self, request, obj, form, change):
		obj.picture = upload_file(request, 'picture')
		super().save_model(request, obj, form, change)


admin.site.register(Member, MemberAdmin)
admin.site.register(Team, TeamAdmin)
