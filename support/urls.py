from . import views
from django.urls import path

app_name = "support"

urlpatterns = [
    path('', views.render_support, name="render_support" ),
]
