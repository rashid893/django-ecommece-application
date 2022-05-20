from django.contrib import admin


from home.models import Products
from .models import Products,Customer,Cart,OrderPlaced
# Register your models here.
admin.site.register(Products)
admin.site.register(Customer)
admin.site.register(Cart)
admin.site.register(OrderPlaced)

# Register your models here.
