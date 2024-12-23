from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, "e_commerce_app/home.html")

def signup(request):
    return render(request, "e_commerce_app/signup.html")


def login(request):
    return render(request, "e_commerce_app/login.html")