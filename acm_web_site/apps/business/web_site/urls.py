from django.urls import path
from . import views


handler404 = 'apps.business.web_site.views.page_not_found'

urlpatterns = [
	path('activities/', views.ActivityList.as_view()),
	path('projects/', views.ProjectList.as_view()),
	path('members', views.members),
	path('teams/', views.TeamList.as_view()),
	path('tutorials/', views.TutorialList.as_view()),
	path('activity/<int:id>/', views.ActivityDetail.as_view()),
	path('project/<int:id>/', views.ProjectDetail.as_view()),
	path('tutorial/<int:id>/', views.TutorialDetail.as_view()),
	# TODO: Create the url for handle reg activity
]
