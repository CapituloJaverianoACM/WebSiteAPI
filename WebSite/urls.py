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
	path('sendQuestionEmail/', views.send_question_email),
	path('sendJoinForm/', views.send_join_form),
	re_path(
		'actividad/(?P<id_activity>[0-9]+)/',
		views.activity_detail,
		name='activity_detail'
	),
	re_path(
		'proyecto/(?P<id_project>[0-9]+)/',
		views.project_detail,
		name='project_detail'
	),
	re_path(
		'tutorial/(?P<id_tutorial>[0-9]+)/',
		views.tutorial_detail,
		name='tutorial_detail'
	),
	re_path(r'$', views.page_not_found),
]
