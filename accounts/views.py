from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.mail import send_mail
from django.http import HttpResponse
from . models import GuestUser
from django.core.mail import BadHeaderError, send_mail
from GTech . settings import EMAIL_HOST_USER
from django.db import transactions

class IndexView(TemplateView):
    template_name = "main2.html"

class WebDesignView(TemplateView):
    template_name = "more-web-design.html"

class GraphicsDesignView(TemplateView):
    template_name = "more-graphics-design.html"

class SoftwareDevelopmentView(TemplateView):
    template_name = "more-software-development.html"

@transaction.atomic
def ContactFormView(request):
    if request.method == 'POST':
        name = request.POST['user_name']
        email = request.POST['user_email']
        message = request.POST['user_message']
        
        
        ins = GuestUser(first_name=name, email_address=email, message=message)
        ins.save()


        send_mail(email, message, EMAIL_HOST_USER, ['geraldoduo@gmail.com'])   
        return render(request, 'contact-response.html', {'name': name})

        
  
        


            
    

 

    




































    

# Create your views here.
