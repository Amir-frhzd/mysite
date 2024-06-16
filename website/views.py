from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from website.models import Contact
from website.forms import NameForm,ContactForm,NewsletterForm
from django.contrib import messages
def index_view(request):

    return render(request,'website/index.html')

def about_view(request):

    return render(request,'website/about.html')

def contact_view(request):
    if request.method == 'POST' :
        form =ContactForm(request.POST)
        if form.is_valid():
            form.cleaned_data['name'] = 'UNKNOWN'
            
            contact=Contact(name=form.cleaned_data['name'],
            
            email = form.cleaned_data['email'],
            
            subject = form.cleaned_data['subject'],
            message = form.cleaned_data['message'])
            contact.save()
            messages.add_message(request,messages.SUCCESS,"Your ticket submited sucssesfully")
        else :
            messages.add_message(request,messages.ERROR,"Your ticket did not sbmited")
    form = ContactForm()
    


    return render(request,'website/contact.html',{'form':form})


def test_view(request):
    if request.method == 'POST':
        form =ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,"DONE")
        else :
            messages.add_message(request,messages.ERROR,"DIDNT DONE")

    form = ContactForm()
    return render(request,'test.html',{'form':form})

def newsletter_view(request):
    if request.method == "POST" :
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,"DONE")
        
            return HttpResponseRedirect('/')
        else:
            messages.add_message(request,messages.ERROR,"Thera is problem")
    else:
        return HttpResponseRedirect('/')

def  under_construction(request):
    return render(request,'website/template.html')       
# Create your views here.
