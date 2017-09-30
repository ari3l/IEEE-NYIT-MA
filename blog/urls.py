from django.conf.urls import url, include
from . import views


urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^team', views.team, name='team'),
    url(r'^project', views.project, name='project'),
    url(r'^completed', views.completed, name='completed'),
    url(r'^post_list$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^signup', views.signup, name='signup'),

]