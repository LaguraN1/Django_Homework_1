from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ProfileForm

def register(request):
    form = UserCreationForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, 'Registration successful!')
        return redirect("main:login")
    return render(request, "main/register_students.html")

def register(request):
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful! You can now log in.')
            return redirect("main:login")
    return render(request, "main/register_students.html", {"form": form})

def login_view(request):
    form = AuthenticationForm(data=request.POST or None)
    if request.method == "POST" and form.is_valid():
        login(request, form.get_user())
        return redirect("main:home")
    return render(request, "main/logIn.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect("main:login")

@login_required(login_url="main:login")
def home(request):
    return render(request, "main/home.html")

@login_required(login_url="main:login")
def profile(request):
    form = ProfileForm(request.POST or None, instance=request.user)
    
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Your profile has been updated!")
        return redirect("main:profile")
        
    return render(request, "main/profile.html", {"form": form})

@login_required(login_url="main:login")
def about(request):
    return render(request, "main/about.html")

@login_required(login_url="main:login")
def profile(request):
    form = ProfileForm(request.POST or None, instance=request.user)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Profile updated!")
    return render(request, "main/profile.html", {"form": form})