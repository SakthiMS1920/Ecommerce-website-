"""
URL configuration for BAS_kart project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include

from django.conf import settings  # import settings to access the file locations
from django.conf.urls.static import static # here importing url of static files from static foleder in settings.py


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('BS_shop.urls')),
]
 
 # here registering the urls for media files from settings
if settings.DEBUG: #
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT ) #caling static function and fetching media url and media root from settigs