from distutils.command.upload import upload
from unicodedata import category
from cv2 import convexityDefects
from django.db import models
from django.contrib.auth.models import User
from numpy import product
from platformdirs import user_cache_dir

category_choices=(
    ('M','Mobile'),
    ('L','lapot'),
    ('TW','Top Wear'),
    ('BW','Bottom War'),
)
categoryr_choices=(
    (' Ratotoder','Ratoder'),
    ('Larkana','Larkana'),
    ('karachi','Karahi'),
    ('Sukkur','Suklkur'),
)
# Cr
# eate your models here.
class Products(models.Model):
    title=models.CharField(max_length=121)
    sellingprice=models.FloatField()
    discount_price=models.FloatField()
    description=models.TextField()
    brand=models.CharField(max_length=121)
    category=models.CharField(choices=category_choices,max_length=2)
    product_image=models.ImageField(upload_to="proudctimages")
    def __str__(self):
        return str(self.id)

class Customer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=122)
    city =models.CharField(max_length=122)
    locality=models.CharField(max_length=122)
  
    state=models.CharField(choices=categoryr_choices,max_length=55)
    def __str__(self):
        return str(self.id)
class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    quantity=models.PositiveBigIntegerField(default=1)
    def __str__(self):
        return str(self.id)
    @property
    def total_cost(self):
        return self.quantity*self.product.discount_price
statechoices=(
    (' Accepted','Accepted'),
    ('packed','packed'),
    ('on thed way','on the way'),
    ('cancel','cancel'),
)
class OrderPlaced(models.Model):
       user=models.ForeignKey(User,on_delete=models.CASCADE)
       customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
       product=models.ForeignKey(Products,on_delete=models.CASCADE)
       quantity=models.PositiveBigIntegerField(default=1)
       orderd_date=models.DateTimeField(auto_now_add=True)
       status=models.CharField(max_length=55,choices=statechoices,default='pending')
       def __str__(self):

           return str(self.id)
       @property
       def total_cost(self):

            return self.quantity*self.product.discount_price

