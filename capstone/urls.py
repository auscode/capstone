"""capstone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('ottanime.urls')),
    # all-auth url needed  for all authenticationBackend configurations
    path('', include('allauth.urls')),
    path('', include('django.contrib.auth.urls')),
]

# These are used for storing user-uploaded files like images, videos, etc
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
# this code is adding URL patterns for serving static and media files when the settings.DEBUG variable is True during development. 
# When the settings.DEBUG variable is False, these URL patterns will not be added, 
# this is helpful during deployment when the files are served by web server directly rather than by the web application.
