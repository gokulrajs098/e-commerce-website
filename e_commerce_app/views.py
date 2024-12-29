from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.contrib.auth import authenticate, login, logout
from .forms import SignupForm, LoginForm, ProductForm, UpdateForm
from .models import User, Product, Reviews
from django.utils import timezone
from datetime import timedelta

def superuser_required(user):
    return user.is_superuser

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
            messages.success(request, "Account created successfully")
            messages.success(request, "Welcome to Gokul-Kart")
            return redirect('login')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    
    return render(request, "e_commerce_app/signup.html")

def login_view(request):
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

def logout_view(request):
    logout(request)

    return redirect('login')

@login_required
def profile(request):
    id = request.user.id
    user = request.user
    if request.method =="PATCH":
        form = UpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save(user=user)
    user = User.objects.get(id=id)
    return render(request, 'e_commerce_app/profile.html', {"user":user})

@login_required
@user_passes_test(superuser_required)
def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data('name')
            price = form.cleaned_data('price')
            quantity = form.cleaned_data('quantity')
            image = form.cleaned_data('image')
            description = form.cleaned_data('description')
            discount = form.cleaned_data('discount')
            Product.objects.create(
                name=name,
                price=price,
                quantity = quantity, 
                image = image, 
                description = description,
                discount = discount
            )
    products = Product.objects.all()
    return render(request, "e_commerce_app/admin_dashboard.html", {"products":products})

def products_view(request, category=None):
    if category:
        products = Product.objects.filter(category=category)
        return render(request, 'e_commerce_app/products.html', {"products":products})
    elif category == "latest":
        now = timezone.now()
        time = now - timedelta(days=2)
        products = Product.objects.filter(created_at__gte=time)
        return render(request, 'e_commerce_app/products.html', {"products":products})
    else:
        return render(request, 'e_commerce_app/products.html')

def product_view(request, id):
    product = Product.objects.filter(id=id)
    return render(request, 'e_commerce_app/product.html', {"product":product})