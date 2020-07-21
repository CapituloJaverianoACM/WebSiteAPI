from django.db import models

# Create your models here.

POSITION_CHOICES = (
    ('1PRE', 'Presidente'),
    ('2VIC', 'Vice-Presidente'),
    ('3SEC', 'Secretario'),
    ('4TES', 'Tesorero'),
    ('5CM', 'Comunity Manager'),
    ('6ME', 'Miembro'),
)

MAJOR_CHOICES = (
    ('IS', 'Ingeniería de Sistemas'),
    ('IE', 'Ingeniería Electrónica'),
    ('II', 'Ingeniería Industrial'),
    ('IC', 'Ingeniería Civil'),
    ('MT', 'Matemáticas'),
    ('OT', 'Otro')
)

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

