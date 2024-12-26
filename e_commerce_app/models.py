from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('user', 'User'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')
    created_at = models.DateTimeField(auto_now_add=True)
    address = models.TextField(blank=True)
    phone_number = models. CharField(null=True, blank=True, max_length=50)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [ 'username']

    def __str__(self):
        return self.username
    
class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=50)
    price = models.FloatField(default=0.0)
    quantity =models.IntegerField(default=0)
    category = models.CharField(max_length=50)
    image = models.ImageField(upload_to="images/")
    description = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    discount = models.FloatField(default=0.0, null=True, blank=True)

    def __str__(self):
        return self.name
    
class Reviews(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    rating = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}-{self.product.name}-{self.rating}"
    
