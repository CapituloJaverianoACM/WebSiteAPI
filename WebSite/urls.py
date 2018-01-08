from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name ='index'),
    url(r'^staff/$', views.staff, name ='staff'),
    url(r'^maratones/$', views.contest, name ='contest'),
    url(r'^actividades/$', views.activities, name ='activities'),
    url(r'^actividad/(?P<idActivity>[0-9]+)$', views.activityDetail, name ='activityDetail'),
    url(r'^proyectos/$', views.projects, name ='projects'),
    url(r'^proyecto/(?P<idProject>[0-9]+)$', views.projectDetail, name ='projectDetail'),
    url(r'^tutoriales/$', views.tutorials, name ='tutorials'),
    url(r'^tutorial/(?P<idTutorial>[0-9]+)$', views.tutorialDetail, name ='tutorialDetail'),
    url(r'^contactUs/$', views.contactUs, name ='contactUs'),
]
