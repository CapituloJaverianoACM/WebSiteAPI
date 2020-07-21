from django.urls import path, include

urlpatterns = [
    path('activities/', include('apps.business.activities.urls')),
]
