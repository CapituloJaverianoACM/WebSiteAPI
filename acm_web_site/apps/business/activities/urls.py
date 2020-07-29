from django.urls import path
from . import views

handler404 = 'business.activities.views.page_not_found'

urlpatterns = [
    path('activities/', views.ActivityList.as_view()),
    path('projects/', views.ProjectList.as_view()),
    path('tutorials/', views.TutorialList.as_view()),
    path('activities/<int:id>/', views.ActivityDetail.as_view()),
    path('projects/<int:id>/', views.ProjectDetail.as_view()),
    path('tutorials/<int:id>/', views.TutorialDetail.as_view()),
    path('register/<int:id>/', views.RegisterActivityView.as_view()),
    # TODO - This URL might change
]
