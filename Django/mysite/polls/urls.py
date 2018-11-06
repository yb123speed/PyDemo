from django.urls import path
from django.conf.urls import url

from . import views
from .views import DetailView, IndexView, ResultsView

app_name = 'polls' # register polls namespace
urlpatterns = [
    path('', views.index, name = 'index'),
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    url('index2/', views.index2, name= 'index2'),
    # ex: /polls/5/
    url(r'^detail2/(?P<question_id>[0-9]+)/$', views.detail2, name='detail2'),
    # url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('IndexView', IndexView.as_view(), name='Index-View'),
    path('DetailView', DetailView.as_view(), name='Detail-View'),
    path('ResultsView', ResultsView.as_view(), name='Results-View'),
]