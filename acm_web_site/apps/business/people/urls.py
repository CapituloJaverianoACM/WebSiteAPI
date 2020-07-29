from django.urls import path
from . import views

handler404 = 'business.people.views.page_not_found'

urlpatterns = [
	path('members', views.MemberViewSet.as_view(dict(get='list'))),
	path('teams/', views.TeamList.as_view()),
	path('joinus/', views.MemberViewSet.as_view(dict(post='create'))),

]
