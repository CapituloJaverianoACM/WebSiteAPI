from django.urls import path, re_path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('staff/', views.staff, name='staff'),
	path('maratones/', views.contest, name='contest'),
	path('actividades/', views.activities, name='activities'),
	path('proyectos/', views.projects, name='projects'),
	path('tutoriales/', views.tutorials, name='tutorials'),
	path('contactUs/', views.contact_us, name='contactUs'),
	path('sendQuestionEmail/', views.sendQuestionEmail),
	path('sendJoinForm/', views.sendJoinForm),
	re_path(
		'actividad/(?P<idActivity>[0-9]+)/',
		views.activity_detail,
		name='activityDetail'
	),
	re_path(
		'proyecto/(?P<idProject>[0-9]+)/',
		views.project_detail,
		name='projectDetail'
	),
	re_path(
		'tutorial/(?P<idTutorial>[0-9]+)/',
		views.tutorial_detail,
		name='tutorialDetail'
	),
	re_path(r'', views.page_not_found),
]
