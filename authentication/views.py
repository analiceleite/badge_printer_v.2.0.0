from .forms import ChangePasswordForm, EDVForm, TokenForm
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.core.cache import cache
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from .utils import send_email

def login(request):
    return render(request, 'registration/login.html')

def request_email(request):
    if request.method == "POST":
        form = EDVForm(request.POST)
        if form.is_valid():
            edv = form.cleaned_data["edv"]
            try:
                user = get_object_or_404(User, username=edv)
                if user != None:
                    send_email(user.email, request)
                    cache.set("user", user, timeout=300)
            except:
                pass
            return redirect("authentication:validate_token")
    else:
        form = EDVForm()
    return render(request, 'request_email.html', {"form": form})

def new_password(request):
    if request.method == "POST":
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            new_password = form.cleaned_data["new_password"]
            confirm_password = form.cleaned_data["confirm_password"]
            if new_password == confirm_password:
                user = cache.get('user')
                user.set_password(new_password)
                user.save()
                cache.delete('user')
                return redirect("authentication:login")
    else:
        form = ChangePasswordForm()
    return render(request, 'new_password.html')

def validate_token(request):
    if request.method == "POST":
        form = TokenForm(request.POST)
        if form.is_valid():
            user_token = form.cleaned_data["token"]
            random_token = request.session.get("randomToken")
            if int(user_token) == random_token:
                request.session.clear()
                return redirect("authentication:new_password")
            form.add_error("token", "Token inválido")
    else:
        form = TokenForm()
    return render(request, 'validate_token.html', {"form": form})

def logout_view(request):
    logout(request)
    return redirect(reverse('authentication:login'))