from django.urls import path
from . import views


handler404 = 'views.page_not_found'

urlpatterns = [
	path('contactus/', views.send_question_email),
	path('members/', views.MemberList.as_view()),
	path('staff/', views.StaffList.as_view()),
	path('activities/', views.ActivityList.as_view()),
	path(
		'tutorial/<str:id_tutorial>/',
		views.tutorial_detail,
	),
	path('test/', views.test)
]
