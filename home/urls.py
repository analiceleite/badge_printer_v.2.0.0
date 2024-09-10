from . import views
from django.urls import path

app_name = "home"

urlpatterns = [
    path('', views.home, name="home" ),
    path('support/', views.support, name="support" ),
    path('error_404/', views.error_404, name="error_404" ),
]
