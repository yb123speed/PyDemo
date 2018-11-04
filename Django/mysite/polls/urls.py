from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    url('index2/', views.index2, name= 'index2'),
    # ex: /polls/5/
    url(r'^detail2/(?P<question_id>[0-9]+)/$', views.detail2, name='detail2'),
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]