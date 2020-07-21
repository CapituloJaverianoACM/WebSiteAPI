from django.db import models

# Create your models here.


class Award(models.Model):
    date = models.DateField()
    picture = models.CharField(max_length=500)
    description = models.CharField(max_length=100)
    title = models.CharField(max_length=100)

    def __str__(self):
        return '%s' % self.picture
