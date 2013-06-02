from django.conf.urls import patterns, include, url
from rest_framework import routers
from chore import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'periods', views.PeriodViewSet)
router.register(r'chores', views.ChoreViewSet)
router.register(r'scores', views.ScoreViewSet)


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'chorescore.views.home', name='home'),
    # url(r'^chorescore/', include('chorescore.foo.urls')),

    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # no idea why the quickstart uses router and tutorial uses normal url
    url(r'^api/users/(?P<user_id>[0-9]+)/periods/(?P<period_id>[0-9]+)/chores/$',
        views.UserPeriodChores.as_view(),
        name='user-period-chore'),
#    url(r'^api/score/$',
#        views.ScoreList.as_view(),
#        name='score'),

    url(r'^rest-api/', include('rest_framework_docs.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
