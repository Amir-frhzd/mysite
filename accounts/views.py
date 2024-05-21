from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from .backends import EmailOrUsernameModelBackend
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

def login_view(request):
    if not request.user.is_authenticated:
        
        if request.method == 'POST':
            
            form = AuthenticationForm(request=request, data=request.POST)
            
            if form.is_valid():
                
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
            
                
                user = EmailOrUsernameModelBackend.authenticate(request, username=username,password=password)
                

                if user is not None:
                    login(request, EmailOrUsernameModelBackend.get_user)
                    messages.add_message(request,messages.SUCCESS,"Your ticket submited sucssesfully")
                    return redirect('/')
        form=AuthenticationForm()
        context ={'form':form}
        
        return render(request,'accounts/login.html',context)
    else :
        return redirect('/')
        messages.add_message(request,messages.ERROR,"Your ticket did not sbmited")
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