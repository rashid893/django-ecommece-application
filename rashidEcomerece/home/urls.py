
from re import template
from xml.dom.minidom import Document
from django.urls import path,include
from home import views
from django.conf import settings
from django.conf.urls.static import static
from home.forms import LoginForm,Mychangepassword

from home.views import  Produtview,Productdetail,CustomerRegisterView,Profileview
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from .forms import LoginForm, Mychangepassword,Mypasswordreset,Myresetform
from rashidEcomerece.settings import MEDIA_ROOT, MEDIA_URL
urlpatterns = [
      path('',views. Produtview.as_view(),name="home"),
    # path('',views.home,name="home"),
    path('pdi<int:pk>/',views.Productdetail.as_view(),name="pdi"),
    path('add_to_cart/',views.add_to_cart,name="add_to_cart"),
     path('show_cart/',views.show_cart,name="show_cart"),
    path('buy_now/',views.buy_now,name="buy_now"),
    path('profile/',views.Profileview.as_view(),name="profile"),
    path('address',views.address,name="address"),
    path('orders',views.orders,name="orders"),
    path('change_password',auth_views.PasswordChangeView.as_view(template_name='changepassword.html',success_url='/passwordchangedone',form_class=Mychangepassword),name="change_password"),
    path('mobile/',views.mobile,name="mobile"),
    path('login/',auth_views.LoginView.as_view(template_name='login.html',authentication_form=LoginForm),name="login"),
    path('customerregistration',views. CustomerRegisterView.as_view(),name="customerregistration"),
    path('checkout',views.checkout,name="checkout"),
     path('payment/',views.payment,name="payment"),
    path("logout/",auth_views.LogoutView.as_view(next_page='login'),name="logout"),
    path("passwordchangedone/",auth_views.PasswordChangeDoneView.as_view(template_name="passwordchange.html"),name="passwordchange"),
    #password reset
    
   
    path('password-reset',auth_views.PasswordResetView.as_view(template_name='password_reset.html',form_class=Mypasswordreset),name="password-reset"),
    path('password-reset-done',auth_views.PasswordResetDoneView.as_view(template_name='password_done.html'),name="password_reset_done"),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='password-reset-confirm.html',form_class=Myresetform),name="password-reset-confirm"),
   #path('reset_password_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password-reset-confirm.html',form_class=Myresetform), name='reset_password_confirm')
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_confirm.html'),name="password_reset_complete"),
   
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
#path('accounts/reset_password_confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='reset_password_confirm')