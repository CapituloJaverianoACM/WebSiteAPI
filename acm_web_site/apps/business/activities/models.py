from django.db import models
from markdownx.models import MarkdownxField
from ..people.models import Member

POSITION_CHOICES = (
    ('1PRE', 'Presidente'),
    ('2VIC', 'Vice-Presidente'),
    ('3SEC', 'Secretario'),
    ('4TES', 'Tesorero'),
    ('5CM', 'Comunity Manager'),
    ('6ME', 'Miembro'),
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


class ActivityMember(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    is_confirmed = models.BooleanField(default=False)


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
