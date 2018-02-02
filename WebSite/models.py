# -- coding: utf-8
from __future__ import unicode_literals

from django.db import models
from django.contrib import admin
from django.core.files.storage import FileSystemStorage

from markdownx.models import MarkdownxField

from .forms import *


EXT_CHOICES = (
	('img', 'Image'),
	('md', 'Markdown'),
	('mdf', 'MarkdownForm'),
	('json', 'JSON'),
	('ot', 'Other'),
)


POSITION_CHOICES = (
	('1PRE', 'Presidente'),
	('2VIC', 'Vice-Presidente'),
	('3SEC', 'Secretario'),
	('4TES', 'Tesorero'),
	('5CM', 'Comunity Manager'),
	('6ME', 'Miembro'),
)

CATEGORY_CHOICES = (
	('NAC', 'Maratón Nacional'),
	('REG', 'Maratón Regional'),
	('MUN', 'Maratón Mundial'),
)

ROLE_CHOICES = (
	('ENC', 'Encargado'),
	('AYU', 'Ayudante'),
	('PAR', 'Participante'),
)

MAJOR_CHOICES = (
	('IS', 'Ingeniería de Sistemas'),
	('IE', 'Ingeniería Electrónica'),
	('II', 'Ingeniería Industrial'),
	('IC', 'Ingeniería Civil'),
	('MT', 'Matemáticas'),
	('OT', 'Otro')
)


class File(models.Model):
	# TODO: Basename is the directory of the file ex: awards/
	basename = models.CharField(max_length=200, default='')
	path = models.CharField(max_length=200)
	ext = models.CharField(max_length=10, choices=EXT_CHOICES)

	def __str__(self):
		return '%s' % self.path


class FileAdmin(admin.ModelAdmin):
	form = FileAdminForm

	def save_model(self, request, obj, form, change):
		file_form = request.FILES['path']
		fs = FileSystemStorage()
		filename = fs.save(obj.basename + file_form.name, file_form)
		uploaded_file_url = fs.url(filename)
		obj.path = uploaded_file_url
		super().save_model(request, obj, form, change)


class Award(models.Model):
	date = models.DateField()
	id_file = models.OneToOneField(File, on_delete=models.CASCADE)
	description = models.CharField(max_length=100)

	def __str__(self):
		return '%s' % (self.id_file.path)


class Member(models.Model):
	name = models.CharField(max_length=200)
	surname = models.CharField(max_length=200)
	email = models.EmailField(unique=True)
	major = models.CharField(max_length=50, choices=MAJOR_CHOICES)
	identification = models.CharField(max_length=50, null=True)
	date_major = models.DateField(null=True)
	date_chapter = models.DateField(null=True)
	date_birth = models.DateField(null=True)
	cellphone = models.CharField(max_length=20, null=True)
	id_photo = models.OneToOneField(File, null=True, on_delete=models.CASCADE)
	is_staff = models.BooleanField(default=False)
	position = models.CharField(max_length=5, choices=POSITION_CHOICES, null=True)
	description = models.CharField(max_length=100, null=True)
	reason = models.TextField(null=True)


class Team(models.Model):
	name = models.CharField(max_length=200)
	id_file = models.OneToOneField(File, on_delete=models.CASCADE)
	members = models.ManyToManyField(
		Member,
		related_name='teams',
		through='TeamMember'
	)


class Contest(models.Model):
	category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
	date = models.DateField()
	place = models.IntegerField()
	teams = models.ManyToManyField(Team, related_name='contests')


class Tutorial(models.Model):
	name = models.CharField(max_length=500)
	information = MarkdownxField()
	files = models.ManyToManyField(File, related_name='tutorials')


class Activity(models.Model):
	name = models.CharField(max_length=500)
	date = models.DateTimeField()
	place = models.CharField(max_length=500)
	members = models.ManyToManyField(
		Member,
		related_name='activities',
		through='ActivityMember'
	)
	information = MarkdownxField()
	files = models.ManyToManyField(File, related_name='activities')
	capacity = models.SmallIntegerField()


class Project(models.Model):
	date_start = models.DateField()
	date_end = models.DateField()
	name = models.CharField(max_length=200)
	members = models.ManyToManyField(Member, related_name='projects')
	information = MarkdownxField()
	files = models.ManyToManyField(File, related_name='projects')


class TeamMember(models.Model):
	team = models.ForeignKey(Team, on_delete=models.CASCADE)
	member = models.ForeignKey(Member, on_delete=models.CASCADE)
	year = models.DateField()


class ActivityMember(models.Model):
	activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
	member = models.ForeignKey(Member, on_delete=models.CASCADE)
	role = models.CharField(max_length=10, choices=ROLE_CHOICES)
	is_confirmed = models.BooleanField(default=False)
