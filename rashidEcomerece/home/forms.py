from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,PasswordChangeForm,PasswordResetForm,SetPasswordForm
from django.contrib.auth.models import User
from django.contrib.auth import password_validation
from django.utils.translation import gettext,gettext_lazy as _
from .models import Customer

# from matplotlib import widget
class CustomerRegistrationForm(UserCreationForm):
    password1: forms.CharField(label=("Password"),strip=False,widget=forms.PasswordInput(attrs={'class':'form-control'}))

    password2: forms.CharField(label=("confrom password"),strip=False,widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email: forms.CharField(label=("EMail"),required=True,strip=False,widget=forms.EmailInput(attrs={'class': 'form-control'}))
  
class Meta:
    model=User
    fields=['username','email','password1','password2']
    labels={'email':'Email'}
    widgets={'username':forms.TextInput(attrs={'class':'form-control'})}
class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label=_("Password"),strip=False,widget=forms.PasswordInput(attrs={'class':'form-control'}))
    

class Mychangepassword(PasswordChangeForm):
    old_password = forms.CharField(label=_ (" Old Password"),strip=False,widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password1 = forms.CharField(label=_(" NewPassword"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'}),help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label=_(" confrom Password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'confrom-password','class':'form-control'}))
class Mypasswordreset(PasswordResetForm):
    email=forms.EmailField(label=_("Email"),max_length=254,widget=forms.EmailInput(attrs={'autocomplete':'email','class':'form-control'}))
class Myresetform(SetPasswordForm):
     new_password1 = forms.CharField(label=_(" NewPassword"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'}),help_text=password_validation.password_validators_help_text_html())
     new_password2 = forms.CharField(label=_(" confrom Password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'confrom-password','class':'form-control'}))
class CustomerProfileview(forms.ModelForm):
     class Meta:
        model=Customer
        fields=['name','locality','city','state']
        widgets={'name':forms.TextInput(attrs={'class':'form-control'}),'locality':forms.TextInput(attrs={'class':'form-control'}),
       'city':forms.TextInput(attrs={'class':'form-control'}),
       'state':forms.Select(attrs={'class':'form-control'})}
