# -*- Mode: Python -*-
# vi:si:et:sw=4:sts=4:ts=4

from chore import models

from django.contrib.auth.models import User, Group


from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class PeriodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Period
        fields = ('url', 'name', )

class ChoreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Chore
        fields = ('url', 'description' )


class ScoreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Score
        fields = ('like', 'weight', 'count', 'chore' )


