from django.db import models
from django.core import validators

from django.contrib.auth import models as amodels

# Create your models here.

class Period(models.Model):

    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

class Chore(models.Model):

    description = models.CharField(max_length=200)

    def __unicode__(self):
        return self.description


class Score(models.Model):

    def __unicode__(self):
        return u'<Score weight %d, %s>' % (self.weight,
            self.like and 'like' or 'not/dislike')

    user = models.ForeignKey(amodels.User)
    period = models.ForeignKey(Period)
    chore = models.ForeignKey(Chore)

    like = models.BooleanField()
    weight = models.PositiveIntegerField(
        validators=[
            validators.MaxValueValidator(3),
            validators.MinValueValidator(1)
        ])
    count = models.PositiveIntegerField(default=1)


