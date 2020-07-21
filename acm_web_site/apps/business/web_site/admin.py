from django.contrib import admin

from django.core.files.storage import FileSystemStorage

from .models import *
from .forms import (
	GalleryAdminForm,
	AwardAdminForm,
	ActivityAdminForm,
	ProjectAdminForm,
	TutorialAdminForm
)


class GalleryAdmin(admin.ModelAdmin):
	form = GalleryAdminForm

	def save_model(self, request, obj, form, change):
		file_form = request.FILES['picture']
		fs = FileSystemStorage()
		filename = fs.save(file_form.name, file_form)
		uploaded_file_url = fs.url(filename)
		obj.picture = uploaded_file_url
		super().save_model(request, obj, form, change)


class AwardAdmin(admin.ModelAdmin):
	form = AwardAdminForm

	def save_model(self, request, obj, form, change):
		file_form = request.FILES['picture']
		fs = FileSystemStorage()
		filename = fs.save(file_form.name, file_form)
		uploaded_file_url = fs.url(filename)
		obj.picture = uploaded_file_url
		super().save_model(request, obj, form, change)


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


admin.site.register(Contest)
admin.site.register(Award, AwardAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Tutorial, TutorialAdmin)
admin.site.register(Activity, ActivityAdmin)
admin.site.register(Project, ProjectAdmin)
# admin.site.register(TeamContest)
# admin.site.register(TutorialFile)
# admin.site.register(ActivityFile)
# admin.site.register(ActivityMember)
# admin.site.register(ProjectFile)
# admin.site.register(ProjectMember)
# admin.site.register(TeamMember)
