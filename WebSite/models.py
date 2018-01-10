from django.db import models
from django.contrib import admin
from django import forms
from django.core.files.storage import FileSystemStorage
from .forms import *

class File(models.Model):
	EXT_CHOICES = (
		('img','Image'),
		('md', 'Markdown'),
		('mdf', 'MarkdownForm'),
		('json', 'JSON'),
		('ot','Other'),
	)
	#TODO: Basename is the directory of the file ex: awards/
	basename = models.CharField(max_length=200, default='')
	path = models.CharField(max_length=200)
	ext = models.CharField(max_length=10, choices=EXT_CHOICES)
	def __str__(self):
		return '%s' % (self.path)

class FileAdmin(admin.ModelAdmin):
	form = FileAdminForm
	def save_model(self, request, obj, form, change):
		fileForm = request.FILES['path']
		fs = FileSystemStorage()
		filename = fs.save(obj.basename + fileForm.name, fileForm)
		uploaded_file_url = fs.url(filename)
		obj.path = uploaded_file_url
		super().save_model(request, obj, form, change)

class Award(models.Model):
	date = models.DateField()
	idFile = models.OneToOneField(File, on_delete=models.CASCADE)
	def __str__(self):
		return '%s' % (self.idFile.path)

class Contest(models.Model):
	CATEGORY_CHOICES = (
		('NAC','Maratón Nacional'),
		('REG', 'Maratón Regional'),
		('MUN', 'Maratón Mundial'),
	)
	category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
	date = models.DateField()
	place = models.IntegerField()

class Team(models.Model):
	name = models.CharField(max_length=200)
	idFile = models.OneToOneField(File, on_delete = models.CASCADE)

class Member(models.Model):
	name = models.CharField(max_length=200)
	surname = models.CharField(max_length = 200)
	email = models.EmailField()
	major = models.CharField(max_length=200)
	identification = models.CharField(max_length=50)
	dateMajor = models.DateField()
	dateChapter = models.DateField()
	dateBirth = models.DateField()
	cellphone = models.CharField(max_length=20)
	idPhoto = models.OneToOneField(File, on_delete=models.CASCADE)

class TeamContest(models.Model):
	idTeam = models.ForeignKey(Team, on_delete = models.CASCADE)
	idContest = models.ForeignKey(Contest, on_delete = models.CASCADE)

class TeamMember(models.Model):
	idTeam = models.ForeignKey(Team, on_delete = models.CASCADE)
	idMember = models.ForeignKey(Member, on_delete = models.CASCADE)
	year = models.DateField()

class Tutorial(models.Model):
	name = models.CharField(max_length=500)

class TutorialFile(models.Model):
	idTutorial = models.ForeignKey(Tutorial, on_delete = models.CASCADE)
	idFile = models.ForeignKey(File, on_delete = models.CASCADE)

class Activity(models.Model):
	name = models.CharField(max_length=500)
	date = models.DateTimeField()
	place = models.CharField(max_length=500)

class ActivityFile(models.Model):
	idActivity = models.ForeignKey(Activity, on_delete = models.CASCADE)
	idFile = models.ForeignKey(File, on_delete = models.CASCADE)

class ActivityMember(models.Model):
	ROLE_CHOICES = (
		('ENC','Encargado'),
		('AYU', 'Ayudante'),
		('PAR', 'Participante'),
	)
	idActivity = models.ForeignKey(Activity, on_delete = models.CASCADE)
	idMember = models.ForeignKey(Member, on_delete = models.CASCADE)
	role = models.CharField(max_length=10, choices=ROLE_CHOICES)

class Project(models.Model):
	dateStart = models.DateField()
	dateEnd = models.DateField()
	name = models.CharField(max_length=200)

class ProjectFile(models.Model):
	idProject = models.ForeignKey(Project, on_delete = models.CASCADE)
	idFile = models.ForeignKey(File, on_delete = models.CASCADE)

class ProjectMember(models.Model):
	idProject = models.ForeignKey(Project, on_delete = models.CASCADE)
	idMember = models.ForeignKey(Member, on_delete = models.CASCADE)
