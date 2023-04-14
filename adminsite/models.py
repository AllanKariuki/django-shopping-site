from django.db import models
from PIL import Image
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

class ProductCategory(models.Model):
    category_name = models.CharField(max_length= 100)
    description = models.CharField(max_length=250)
    
    def __str__(self):
        return self.category_name

class Brand(models.Model):
    brand_name = models.CharField(max_length= 100)
    description = models.CharField(max_length=250)
    
    def __str__(self):
        return self.brand_name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    image = models.ImageField(upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username}Profile'

    def save(self):
        super().save()
        img= Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (200, 200)
            img.thumbnail(output_size)
            img.save(self.image.path)
            
class Product(models.Model):
    category_name = models.ForeignKey(ProductCategory, on_delete= CASCADE)
    brand_name = models.ForeignKey(Brand, on_delete=CASCADE)
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='products/')
    color = models.CharField(max_length=100)
    price = models.IntegerField()
    quantity = models.IntegerField()
    detail1 = models.CharField(max_length=50)
    detail2 = models.CharField(max_length=50)
    detail3 = models.CharField(max_length=50)
    description = models.CharField(max_length=50, null= True)
    
    def __str__(self):
        return f'{self.name}'

