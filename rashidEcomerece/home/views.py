


from nturl2path import url2pathname
from os import stat
from unicodedata import category
from django.shortcuts import redirect, render,HttpResponse
from numpy import product
from pyrsistent import m
from requests import delete
from .models import Cart, Products,Customer,OrderPlaced
from django.views import View
from .forms import CustomerRegistrationForm,CustomerProfileview
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Q
# Create your v
# 
# 
# iews here
# .


@method_decorator(login_required,name='dispatch')
class Profileview(View):
    def get(self,request):
        form=CustomerProfileview()
        return render (request,'profile.html',{'form':form,'active':'btn-primary'})
    def post(self,request):
        form=CustomerProfileview(request.POST)
        if form.is_valid():
            usr=request.user
            name=form.cleaned_data['name']
            locality=form.cleaned_data['locality']
            city=form.cleaned_data['city']
            state=form.cleaned_data['state']
            reg=Customer(user=usr,name=name,locality=locality,city=city,state=state)
            reg.save()
            messages.success(request,"Your Form Subnited successfully")
        return render (request,'profile.html',{'form':form,'active':'btn-primary'})
        



class Produtview(View):


    def get(self,request):
        products=Products.objects.all()
        print(products)
        topwares=Products.objects.filter(category='TW')
        bottomwares=Products.objects.filter(category='BW')
        mobiles=Products.objects.filter(category='M')
        
        return render (request,'home.html',{'topwares':topwares,'bottomwares':bottomwares,'mobiles':mobiles,'products':products})
def home(request):
    
    return render(request,'home.html')
# def pdi(request):
class Productdetail(View):
    def get(self,request,pk):

        products=Products.objects.get(pk=pk)
        # item_already_in_cart=False
        # if request.user.is_authenticated:

        #     item_already_in_cart=Cart.objects.filter(Q(product=product.id) & Q(user=request.user)).exists()
    
        return render(request,'pdi.html',{'products':products})
def add_to_cart(request):
    user=request.user
    product_id=request.GET.get('product_id')
    product=Products.objects.get(id=product_id)
    Cart(user=user,product=product).save()
    #print(" Pro id And user Name",product_id,user)

    
    # return render(request,'add_to_cart.html')
    return redirect('/show_cart')
def show_cart(request):
    if request.user.is_authenticated:
        user=request.user
        cart=Cart.objects.filter(user=user)
       # print(cart)
        amount=0.0
        shiping_amount=70.0
        total_amount=70.0
        cart_product=[p for p in  Cart.objects.all() if p.user==request.user]
        if cart_product:

            for p in cart_product:
                tempamount=(p.quantity * p.product.discount_price)
                amount += tempamount
                totalamount=amount+shiping_amount
        else:

            return render(request,'empty.html')
       # print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxx",cart_product)

    return render(request,'add_to_cart.html',{'cart':cart,'totalamount':totalamount,'amount':amount})
   
   

def buy_now(request):
    
    return render(request,'buy_now.html')
# def profile(request):
    
#     return render(request,'profile.html')
def address(request):
    add=Customer.objects.filter(user=request.user)
    
    return render(request,'address.html',{'add':add})
@login_required 
def orders(request):
    od=OrderPlaced.objects.filter(user=request.user)

    
    return render(request,'orders.html',{'od':od})
def change_password(request):
    
    return render(request,'changepassword.html')
def mobile(request):
    
    return render(request,'mobile.html')
def login(request):
    
    return render(request,'login.html')
class CustomerRegisterView(View):
    def get(self,request):
        form=CustomerRegistrationForm()
        return render(request,'customerregistration.html',{'form':form})
    def post(self,request):

        form=CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request,'Your Acount Created Succfully')
            form.save()
        return render(request,'customerregistration.html',{'form':form})
        
# def customerregistration(request):
    
#     return render(request,'customerregistration.html')
def checkout(request):
    user=request.user
    add=Customer.objects.filter(user=user)
    cart_item=Cart.objects.filter(user=user)
    amount=0.0
    shiping_amount=70.0
    total_amount=70.0
    cart_product=[p for p in  Cart.objects.all() if p.user==request.user]
    if cart_product:
        for p in cart_product:

            tempamount=(p.quantity * p.product.discount_price)
            amount += tempamount
            totalamount=amount+shiping_amount

    
   
    return render(request,'checkout.html',{'add':add,'totalamount':totalamount,'cart_item':cart_item})
@login_required   
def payment(request):
    user=request.user
    custid=request.GET.get('custad')

  
    customer=Customer.objects.get(id=custid)
    cart=Cart.objects.filter(user=user)
    for c in cart:
        OrderPlaced(user=user,customer=customer,product=c.product,quantity=c.quantity).save()
        c.delete()
        
    return redirect('orders')
        # return render(request,'orders.html')



# Create your models here.
