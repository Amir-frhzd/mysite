from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class login_forms(forms.Form):
    username_or_email =forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta():
        model =User
        field=['username_or_email','password']

class UserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields= ["username", "email", "password1", "password2"]