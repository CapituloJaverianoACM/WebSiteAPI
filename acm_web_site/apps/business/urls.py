from django.urls import path, include

urlpatterns = [
    path('people/', include('apps.business.people.urls')),
    path('information/', include('apps.business.information.urls')),
]
