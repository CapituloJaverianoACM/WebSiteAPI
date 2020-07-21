from django.urls import path, include

urlpatterns = [
    path('activities/', include('apps.business.activities.urls')),
    path('people/', include('apps.business.people.urls')),
    path('information/', include('apps.business.information.urls')),
]
