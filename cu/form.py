from django import forms
from .models import profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class URF(UserCreationForm):
    email=forms.EmailField(help_text='just fill in the correct email address!!!!!!')

    class Meta:
        model=User
        fields=['username','email','password1','password2']

class U_U_f(forms.ModelForm):
    email=forms.EmailField()

    class Meta:
        model=User
        fields=['username','email']


class P_U_f(forms.ModelForm):
   
    class Meta:
        model=profile
        fields=['image']
