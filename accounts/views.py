from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import AuthenticationForm
from .backends import EmailOrUsernameModelBackend
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import login_forms,UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
# Create your views here.

def login_view(request):
    if not request.user.is_authenticated:
        
        if request.method == 'POST':
            form = login_forms(request.POST)
            
            if form.is_valid():
                
                username=form.cleaned_data['username_or_email']
                password=form.cleaned_data['password']
                
                #password=form.cleaned_data['password']
                
                if '@' in username:
                    
                    username = User.objects.get(email=username).username
                else :
                    
                    username = username
                    
                user =authenticate(username=username,password=password)
                
                if user is not None:
                    
                    login(request,user)
                    messages.add_message(request,messages.SUCCESS,"You logedd in sucsess")
                    return redirect('/')
            
                else:
                    messages.add_message(request,messages.ERROR,"username/email or password is wrong")
                    #return redirect('/')            
        form=AuthenticationForm()
        context ={'form':form}
        
        return render(request,'accounts/login.html',context)
    else :
        
        return redirect('/')
        
        
 
@login_required
def logout_view(request):
    logout(request)
    return redirect('/')

def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            
            form =UserCreationForm(request.POST)
            
            if form.is_valid():
                
                form.save()
    
                return redirect('/')
    else:
        return redirect('/')            
    form=UserCreationForm()
    context = {'form':form}
    return render(request,'accounts/signup.html',context)

class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'users/password_reset.html'
    email_template_name = 'users/password_reset_email.html'
    subject_template_name = 'users/password_reset_subject'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('website:index')