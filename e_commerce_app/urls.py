from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('signup/', views.signup, name="signup"),
    path('login/', views.login_view, name="login"),
    path('add_products/', views.add_product, name="add_product"),
    re_path(r'^products/(?P<category>[\w-]+)?$', views.products_view, name="products"),
    path('product/<str:id>', views.product_view, name="product")

]
