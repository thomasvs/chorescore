# -*- Mode: Python -*-
# vi:si:et:sw=4:sts=4:ts=4

from chore import models

from django.contrib.auth.models import User, Group


from rest_framework import serializers

# see http://stackoverflow.com/questions/15014495/id-field-in-django-rest-framework-serializer
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'url', 'name')

class PeriodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Period
        fields = ('id', 'url', 'name', )

class ChoreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Chore
        fields = ('id', 'url', 'description' )


class ScoreFullSerializer(serializers.HyperlinkedModelSerializer):
    """
    I serialize with full related objects.
    Useful for GET, but not for POST.
    """

    chore = ChoreSerializer(many=False)
    user = UserSerializer(many=False)
    group = GroupSerializer(many=False)
    period = PeriodSerializer(many=False)

    class Meta:
        model = models.Score
        fields = (
            'id',
            'chore',
            'user',
            'group',
            'period',
            'like', 'weight', 'count',
        )
        depth = 1

class ScoreIdSerializer(serializers.ModelSerializer):
    """
    I serialize with only id's for objects.
    Useful for POST.
    """

    class Meta:
        model = models.Score
        fields = (
            'id',
            'chore',
            'user',
            'group',
            'period',
            'like', 'weight', 'count',
        )


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Result
        fields = (
            'id',
            'user',
            'group',
            'period',
            'points',
            'total',
        )


