from django.urls import path
from . import views

#by camilo serrano
handler404 = 'apps.business.people.views.page_not_found'

urlpatterns = [
	path('members', views.members),
	path('teams/', views.TeamList.as_view()),
	path('joinus/', views.join_us),

]
