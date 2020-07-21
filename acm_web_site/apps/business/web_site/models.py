# -- coding: utf-8
from __future__ import unicode_literals

from django.db import models
from markdownx.models import MarkdownxField

from ..people.models import Member, Team

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




class ActivityMember(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    is_confirmed = models.BooleanField(default=False)
