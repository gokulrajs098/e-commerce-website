from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .forms import SignupForm, LoginForm
from .models import User


@login_required
def home(request):
    return render(request, "e_commerce_app/home.html")

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            firstname = form.cleaned_data.get('firstname')
            lastname = form.cleaned_data.get('lastname')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = User.objects.create(
                username=username,
                first_name=firstname,
                last_name = lastname,
                email = email,
            )
            user.set_password(password)
            user.save()
            return redirect('home')
        
    return render(request, "e_commerce_app/signup.html")

def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)
            if user:
                login(request, user)
                return redirect('home')
            else:
                print("invalid")
                    
    return render(request, "e_commerce_app/login.html")