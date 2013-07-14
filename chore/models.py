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
        return u'<Score weight %d, %s, completed %d times>' % (self.weight,
            self.like and 'like' or 'not/dislike', self.count)

    class Meta:
        unique_together = ('user', 'group', 'period', 'chore')

    user = models.ForeignKey(amodels.User)
    group = models.ForeignKey(amodels.Group)
    period = models.ForeignKey(Period)
    chore = models.ForeignKey(Chore)

    like = models.BooleanField()
    weight = models.PositiveIntegerField(
        default=0,
        validators=[
            validators.MaxValueValidator(3),
            validators.MinValueValidator(0)
        ])
    # how many times this user completed the task
    count = models.PositiveIntegerField(default=0)

    def points(self):
        """
        Calculate the points this task represents.
        """
        p = self.weight
        if not self.like:
            p *= 2
        return p


class Result(models.Model):

    user = models.ForeignKey(amodels.User)
    group = models.ForeignKey(amodels.Group)
    period = models.ForeignKey(Period)

    points = models.PositiveIntegerField()
    total = models.PositiveIntegerField(default=0)

