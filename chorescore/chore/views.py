# Create your views here.

from chore import models
from chore import serializers

from django.contrib.auth.models import User, Group
from rest_framework import viewsets

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

class PeriodViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = models.Period.objects.all()
    serializer_class = serializers.PeriodSerializer

class UserPeriodChores(viewsets.ModelViewSet):
    """
    API endpoint that allows chores to be seen or added for a given user
    and period.
    """
    serializer_class = serializers.PeriodSerializer

    def get_queryset(self):
            """
            This view should return a list of all the purchases for
            the user as determined by the username portion of the URL.
            """
            user_id = self.kwargs['user_id']
            period_id = self.kwargs['period_id']
            return models.Chore.objects.filter(
                user_id=user_id, period_id=period_id)
