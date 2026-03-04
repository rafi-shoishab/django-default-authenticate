from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    return render(request, 'accounts/index.html')

def register(request):
    return render(request, 'accounts/register.html')

def signin(request):
    return render(request, 'accounts/login.html')

def profile(request):
    return render(request, 'accounts/profile.html')