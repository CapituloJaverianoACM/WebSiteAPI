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


class TeamMember(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    year = models.DateField()
