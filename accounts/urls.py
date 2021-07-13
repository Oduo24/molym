
from django.urls import path, include
from . import views

urlpatterns = [
    path('molymtech.herokuapp.com/',  views.IndexView.as_view(), name="index"),
    path('molymtech.herokuapp.com/web-design', views.WebDesignView.as_view(), name='web-design'),
    path('molymtech.herokuapp.com/graphics-design', views.GraphicsDesignView.as_view(), name='graphics-design'),
    path('molymtech.herokuapp.com/software-development', views.SoftwareDevelopmentView.as_view(), name='software-development'),
    path('molymtech.herokuapp.com/web-design/home', views.IndexView.as_view(), name="back-to-home"),
    path('molymtech.herokuapp.com/web-design/services', views.IndexView.as_view(), name="back-to-home"),
    path('molymtech.herokuapp.com/ContactForm', views.ContactFormView, name="ContactForm"),
    
    

    



]










