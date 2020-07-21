from django.contrib import admin
from django.core.files.storage import FileSystemStorage

from .forms import MemberAdminForm, TeamAdminForm
from .models import Member, Team


class MemberAdmin(admin.ModelAdmin):
	form = MemberAdminForm

	def save_model(self, request, obj, form, change):
		file_form = request.FILES['picture']
		fs = FileSystemStorage()
		filename = fs.save(file_form.name, file_form)
		uploaded_file_url = fs.url(filename)
		obj.picture = uploaded_file_url
		super().save_model(request, obj, form, change)


class TeamAdmin(admin.ModelAdmin):
	form = TeamAdminForm

	def save_model(self, request, obj, form, change):
		file_form = request.FILES['picture']
		fs = FileSystemStorage()
		filename = fs.save(file_form.name, file_form)
		uploaded_file_url = fs.url(filename)
		obj.picture = uploaded_file_url
		super().save_model(request, obj, form, change)


admin.site.register(Member, MemberAdmin)
admin.site.register(Team, TeamAdmin)
