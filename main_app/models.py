from django.db import models
from django.contrib.auth.models import User, AbstractUser
# Create your models here.

class QuoteRequest(models.Model):
    fullname = models.CharField(max_length = 200, null = True, blank=True)
    email = models.EmailField(max_length=250, null=True, blank=True)
    phone_number = models.CharField(max_length=250, null=True, blank=True)
    
    def __str__(self) -> str:
        return str(self.fullname)
    
class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    
class Subscription(models.Model):
    
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    plan_name = models.CharField(max_length=50, blank=True, null=True)
    start_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    end_date = models.DateTimeField(blank=True, null=True)
    next_payment_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=[('Active', 'Active'), ('Inactive', 'Inactive'), ('Cancelled', 'Cancelled')], blank=True, null=True)
    


class Payment_Method(models.Model):
    
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    card_number = models.CharField(max_length=16, null=True, blank=True)
    expiry_date = models.DateField(null=True, blank=True)
    card_holder_name = models.CharField(max_length=50,null=True, blank=True)
    billing_address = models.TextField(null=True, blank=True)
    

class Order(models.Model):
    
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    items = models.TextField(null=True, blank=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Shipped', 'Shipped'), ('Delivered', 'Delivered'), ('Cancelled', 'Cancelled')], null=True, blank=True)
    
class LoginActivity(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    login_time = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    location = models.CharField(max_length=100,null=True, blank=True)
    
class SecurityQuestion(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    question = models.CharField(max_length=100,null=True, blank=True)
    answer = models.CharField(max_length=100,null=True, blank=True)
    
class Service(models.Model):

    name = models.CharField(max_length=50, null=True, blank=False)
    
    def __str__(self):
        return self.name
