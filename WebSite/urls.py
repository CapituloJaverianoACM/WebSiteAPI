from django.urls import path
from . import views


handler404 = 'views.page_not_found'

urlpatterns = [
	path('', views.index, name='index'),
	path('staff/', views.staff, name='staff'),
	path('maratones/', views.contest, name='contest'),
	path('actividades/', views.activities, name='activities'),
	path('proyectos/', views.projects, name='projects'),
	path('tutoriales/', views.tutorials, name='tutorials'),
	path('sendQuestionEmail/', views.send_question_email),
	path('sendJoinForm/', views.send_join_form),
	path(
		'actividad/<str:id_activity>/',
		views.activity_detail,
		name='activity_detail'
	),
	path(
		'proyecto/<str:id_project>/',
		views.project_detail,
		name='project_detail'
	),
	path(
		'tutorial/<str:id_tutorial>/',
		views.tutorial_detail,
		name='tutorial_detail'
	)
]
