from django.contrib import admin
from django.urls import path, include

from markdownx import urls as markdownx

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', include('WebSite.urls')),
	path('markdownx/', include('markdownx.urls')),
]
