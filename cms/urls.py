from django.urls import path, re_path
from cms import views

app_name = "cms"

urlpatterns = [
    path('', views.home, name='home'),                     # ✅ simple path
    re_path(r'^(?P<permalink>.+)$', views.home, name='home')  # ✅ regex path
]
