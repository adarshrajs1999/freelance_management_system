"""
URL configuration for freelancers_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from django.urls import path,include
from django.contrib import admin
from django.urls import path

from freelancers_project.settings import BASE_DIR

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('freelancers_app.urls')),
]

# freelancer_project/urls.py
from django.conf import settings
from django.conf.urls.static import static

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

# Media files for uploaded submissions
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
