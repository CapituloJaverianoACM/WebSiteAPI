from django.urls import path, include

urlpatterns = [
    path('activities/', include('business.activities.urls')),
    path('people/', include('business.people.urls')),
    path('information/', include('business.information.urls')),
]
