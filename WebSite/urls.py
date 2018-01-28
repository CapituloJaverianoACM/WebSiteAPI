from django.urls import path
from . import views


handler404 = 'views.page_not_found'

urlpatterns = [
	path('contactus/', views.send_question_email),
	path('joinform/', views.send_join_form),
	path(
		'tutorial/<str:id_tutorial>/',
		views.tutorial_detail,
	),
	path('test/', views.test)
]
