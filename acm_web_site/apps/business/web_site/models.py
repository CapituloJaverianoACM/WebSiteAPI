# -- coding: utf-8
from __future__ import unicode_literals

from django.db import models
from markdownx.models import MarkdownxField

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


class Gallery(models.Model):
    picture = models.CharField(max_length=200)

    def __str__(self):
        return '%s' % self.picture


class Award(models.Model):
    date = models.DateField()
    picture = models.CharField(max_length=500)
    description = models.CharField(max_length=100)
    title = models.CharField(max_length=100)

    def __str__(self):
        return '%s' % self.picture


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
    picture = models.CharField(max_length=200)
    is_staff = models.BooleanField(default=False)
    position = models.CharField(max_length=5,
                                choices=POSITION_CHOICES,
                                null=True)
    description = models.CharField(max_length=100, null=True)
    reason = models.TextField(null=True)

    def __str__(self):
        return '%s %s' % (self.name, self.surname)


class Team(models.Model):
    name = models.CharField(max_length=200)
    picture = models.CharField(max_length=200)
    members = models.ManyToManyField(
        Member,
        related_name='teams',
        through='TeamMember'
    )

    def __str__(self):
        return '%s' % self.name


class Contest(models.Model):
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    date = models.DateField()
    place = models.IntegerField()
    teams = models.ManyToManyField(Team, related_name='contests')

    def __str__(self):
        date_str = self.date.strftime('%Y-%m-%dT%H:%M:%S')
        return '%s - %s' % (date_str, self.category)


class Tutorial(models.Model):
    name = models.CharField(max_length=500)
    information = MarkdownxField()
    poster = models.CharField(max_length=200)
    gallery = models.ManyToManyField(
        Gallery,
        related_name='tutorials',
        blank=True
    )

    def __str__(self):
        return '%s' % self.name


class Activity(models.Model):
    name = models.CharField(max_length=500)
    date = models.DateTimeField()
    place = models.CharField(max_length=500)
    members = models.ManyToManyField(
        Member,
        related_name='activities',
        through='ActivityMember',
    )
    information = MarkdownxField()
    gallery = models.ManyToManyField(
        Gallery,
        related_name='activities',
        blank=True
    )
    capacity = models.SmallIntegerField()
    poster = models.CharField(max_length=80)
    description = models.CharField(max_length=500)

    def __str__(self):
        date_str = self.date.strftime('%Y-%m-%dT%H:%M:%S')
        return '%s - %s' % (self.name, date_str)


class Project(models.Model):
    date_start = models.DateField()
    date_end = models.DateField()
    name = models.CharField(max_length=200)
    members = models.ManyToManyField(Member, related_name='projects')
    information = MarkdownxField()
    gallery = models.ManyToManyField(
        Gallery,
        related_name='projects',
        blank=True
    )
    poster = models.CharField(max_length=200)
    description = models.CharField(max_length=500)

    def __str__(self):
        return '%s' % self.name


class TeamMember(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    year = models.DateField()


class ActivityMember(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    is_confirmed = models.BooleanField(default=False)
