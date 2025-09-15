"""workshop_portal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path, re_path, include
from django.conf.urls.static import static
from django.contrib import admin
from workshop_portal import views
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),                 # ✅ simple path
    path('', views.index),                           # ✅ homepage
    path('workshop/', include('workshop_app.urls')), # ✅ simple path
    path('reset/', include('django.contrib.auth.urls')),  # ✅ simple path
    path('page/', include('cms.urls')),              # ✅ simple path
    path('statistics/', include('statistics_app.urls')),  # ✅ simple path
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
