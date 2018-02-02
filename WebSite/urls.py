from django.urls import path
from . import views


handler404 = 'views.page_not_found'

urlpatterns = [
	path('contactus/', views.send_question_email),
	path('members/',views.member_list()),
	path('member/<str:id>/',views.member_detail()),
	path('staff/', views.StaffList.as_view()),
	path('activities/', views.ActivityList.as_view()),
	path('activity/<int:id>/', views.ActivityDetail.as_view()),
	path('tutorial/<str:id_tutorial>/', views.tutorial_detail),
	path('test/', views.test)
]
