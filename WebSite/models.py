from django.db import models

class File(models.Model):
    EXT_CHOICES = (
        ('img','Image'),
        ('md', 'Markdown'),
        ('mdf', 'MarkdownForm'),
        ('json', 'JSON'),
        ('ot','Other'),
    )
    path = models.FilePathField(path="/home")
    ext = models.CharField(max_length=10, choices=EXT_CHOICES)

class Award(models.Model):
    date = models.DateField()
    idFile = models.OneToOneField(File, on_delete=models.CASCADE)

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
