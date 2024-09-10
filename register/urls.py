from . import views
from django.urls import path

app_name = "register"

urlpatterns = [
    path('', views.render_register, name="register" ),
]
