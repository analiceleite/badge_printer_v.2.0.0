from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def support(request):
    return render(request, 'support.html')

def error_404(request):
    return render(request, 'exception/error_404.html')
