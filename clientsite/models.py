from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from adminsite.models import Product

class RequestForService(models.Model):
    customer_name = models.ForeignKey(User, on_delete= CASCADE)
    email = models.EmailField()
    phone = models.CharField(max_length= 100)
    company = models.CharField(max_length=100)
    photocopy_model = models.CharField(max_length=100)
    location = models.CharField(max_length=70)
    description = models.CharField(max_length=200)
    
    def __str__(self):
        return self.email

class RequestForQuotation(models.Model):
    customer_name = models.ForeignKey(User, on_delete= CASCADE)
    email = models.EmailField()
    phone = models.CharField(max_length= 100)
    company = models.CharField(max_length=100)
    product = models.CharField(max_length=100)
    additional_remarks = models.CharField(max_length=100)

    def __str__(self):
        return self.company

class CartItem(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

class Order(models.Model):
    date_ordered = models.DateTimeField(auto_now_add=True)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    location = models.CharField(max_length=60)
    phone = models.IntegerField(null= True)
    email = models.EmailField()
    additional_information = models.CharField(max_length=200)

    def __str__(self):
        return f'Order {self.id}'

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.quantity} x {self.product.product_name} ({self.subtotal})'
    