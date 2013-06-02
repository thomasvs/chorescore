# Create your views here.

from chore import models
from chore import serializers

from django.contrib.auth.models import User, Group

from rest_framework import viewsets, generics

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = serializers.GroupSerializer

class ChoreViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = models.Chore.objects.all()
    serializer_class = serializers.ChoreSerializer


class PeriodViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows periods to be viewed or edited.
    """
    queryset = models.Period.objects.all()
    serializer_class = serializers.PeriodSerializer

class ScoreList(generics.ListAPIView):
    """
    API endpoint that allows scores to be viewed or edited.
    """
    serializer_class = serializers.ScoreSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `user_id` and `period_id` query parameter in the
        URL.
        """
        queryset = models.Score.objects.all()
        user_id = self.request.QUERY_PARAMS.get('user_id', None)
        if user_id is not None:
            queryset = queryset.filter(user_id=user_id)
        period_id = self.request.QUERY_PARAMS.get('period_id', None)
        if period_id is not None:
            queryset = queryset.filter(period_id=period_id)
        return queryset

#class UserPeriodChores(viewsets.ModelViewSet):
class UserPeriodChores(generics.ListAPIView):
    """
    API endpoint that allows chores to be seen or added for a given user
    and period.
    """
    serializer_class = serializers.ScoreSerializer

    def get_queryset(self):
            """
            This view should return a list of all the purchases for
            the user as determined by the username portion of the URL.
            """
            user_id = self.kwargs['user_id']
            period_id = self.kwargs['period_id']
            return models.Score.objects.filter(
                user_id=user_id, period_id=period_id)
