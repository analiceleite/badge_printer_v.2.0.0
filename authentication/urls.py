from . import views
from django.contrib.auth import views as auth_views
from django.urls import path

app_name = "authentication"

urlpatterns = [
    path('', auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('forgot-password/', views.request_email, name='request_email'),
    path('forgot-password/token', views.validate_token, name='validate_token'),
    path('forgot-password/new-password', views.new_password, name='new_password'),
    path('logout', views.logout_view, name='logout_view'),
]
