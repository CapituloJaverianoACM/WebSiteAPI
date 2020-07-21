from django.urls import path, include

urlpatterns = [
    path('web_site/', include('apps.business.web_site.urls')),
    path('people/', include('apps.business.people.urls')),
    path('information/', include('apps.business.information.urls')),
]
