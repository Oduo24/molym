from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.mail import send_mail
from django.http import HttpResponse
from . models import GuestUser
from django.core.mail import BadHeaderError, send_mail
from django.conf import settings




def IndexView(request):
    return render(request, 'home/main2.html')

def WebDesignView(request):
    return render(request, 'home/more-web-design.html')

def GraphicsDesignView(request):
    return render(request, 'home/more-graphics-design.html')

def SoftwareDevelopmentView(request):
    return render(request, 'home/more-software-development.html')


def ContactFormView(request):
    if request.method == 'POST':
        name = request.POST['user_name']
        email = request.POST['user_email']
        message = request.POST['user_message']
        
        
        ins = GuestUser(first_name=name, email_address=email, message=message)
        ins.save()


        send_mail(email, message, settings.EMAIL_HOST_USER, ['geraldoduo@gmail.com'])   
        return render(request, 'home/contact-response.html', {'name': name})

        
  
        


            
    

 

    




































    

# Create your views here.
