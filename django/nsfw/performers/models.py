from django.db import models
from django.utils.translation import gettext as _

# Create your models here.


class Performer(models.Model):

    class Gender(models.TextChoices):
        MALE = 'M', _('MALE')
        FEMALE = 'F', _('FEMALE')
        TRANS_M = 'TM', _('TRANS_M')
        TRANS_F = 'TF', _('TRANS_F')
        INTERSEX = 'IS', _('INTERSEX')

    name = models.CharField("Name", max_length=50)
    url = models.URLField(max_length=200)
    gender = models.CharField(max_length=8,
                              choices=Gender.choices,
                              default=Gender.FEMALE)

    aliases = models.CharField("aliases", max_length=150)
    favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.name
