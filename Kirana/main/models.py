from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator

class Category(models.Model):
    category_name = models.CharField(max_length=255)
    category_image = models.ImageField(upload_to='Category')

    def __str__(self):
        return self.category_name
    
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='Product')
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(default=0.00, decimal_places=2, max_digits=6)
    per = models.CharField(default='Kg', max_length=50, null=True, blank=True)
    min_order = models.PositiveIntegerField()
    max_order = models.PositiveIntegerField()
    stock_qty = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Rating(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(validators=[MaxValueValidator(5)])
    review = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.product

# Create your models here.


class form(models.Model):

    username = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length= 30)
    repassword = models.CharField(max_length= 30)

