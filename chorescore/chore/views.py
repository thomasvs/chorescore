# Create your views here.

from chore import models
from chore import serializers

from django.contrib.auth.models import User, Group

from rest_framework import viewsets, generics, decorators, response


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

#class ScoreList(generics.ListAPIView):
class ScoreViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows scores to be viewed or edited.
    """
    serializer_class = serializers.ScoreIdSerializer
    queryset = models.Score.objects.all() # to get the name

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

#    @decorators.action
#    def score(self, *args, **kwargs):
#        print 'THOMAS: score!'
#        return response.Response({'status': 'score set'})

class ScoreFullViewSet(ScoreViewSet):
    """
    API endpoint that allows scores to be viewed in full.
    """
    serializer_class = serializers.ScoreFullSerializer
 
#class UserPeriodChores(viewsets.ModelViewSet):
class UserPeriodChores(generics.ListAPIView):
    """
    API endpoint that allows chores to be seen or added for a given user
    and period.
    """
    serializer_class = serializers.ScoreFullSerializer

    def get_queryset(self):
            """
            This view should return a list of all the purchases for
            the user as determined by the username portion of the URL.
            """
            user_id = self.kwargs['user_id']
            period_id = self.kwargs['period_id']
            return models.Score.objects.filter(
                user_id=user_id, period_id=period_id)

class ResultList(generics.ListAPIView):
    """
    API endpoint that allows results to be shown for a group and period.
    """
    serializer_class = serializers.ResultSerializer
    queryset = models.Score.objects.all() # to get the name

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `group_id` and `period_id` query parameter in the
        URL.
        """
        queryset = models.Score.objects.all()
        user_id = self.request.QUERY_PARAMS.get('user_id', None)
        if user_id is not None:
            queryset = queryset.filter(user_id=user_id)
        group_id = self.request.QUERY_PARAMS.get('group_id', None)
        if group_id is not None:
            queryset = queryset.filter(group_id=group_id)
        period_id = self.request.QUERY_PARAMS.get('period_id', None)
        if period_id is not None:
            queryset = queryset.filter(period_id=period_id)
        #print 'THOMAS; returning', queryset

        scores = {} # dict of (group, period) -> (dict of user -> list of Score)

        # order the scores assigned by each user to each group/period
        for score in queryset:
            key = (score.group, score.period)
            if key not in scores:
                scores[key] = {}
            if score.user not in scores[key]:
                scores[key][score.user] = []
            scores[key][score.user].append(score)


        # now, calculate the score each user has obtained out of the total
        ret = {} # dict of (group, period) -> (dict of user -> Result)
        ret = []
        for (group, period), users in scores.items():
            for user, score_list in users.items():
                total = 0
                points = 0

                # calculate the chore's points for this user as the average
                # of all other votes

                for score in score_list:
                    other_scores = models.Score.objects.filter(
                        group_id=group,
                        period_id=period,
                        chore_id=score.chore.id)
                    chore_points = sum([s.points() for s in other_scores]) / len(other_scores)
                    count = score.count or 1
                    points += chore_points * score.count
                    total += chore_points * count

                ret.append(models.Result(user=user, group=group, period=period,
                    points=points, total=total))

        return ret

#    @decorators.action
#    def score(self, *args, **kwargs):
#        print 'THOMAS: score!'
#        return response.Response({'status': 'score set'})


