from . import views
from django.urls import path

app_name = "import"

urlpatterns = [
    path('', views.import_files, name="import_files"),
]
