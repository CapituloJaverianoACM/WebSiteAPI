from django.urls import path, include

urlpatterns = [
    path('web_site/', include('apps.business.web_site.urls')),
    path('activities/', include('apps.business.activities.urls')),
]
