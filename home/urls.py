
from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView, name='index'),
    path('index/', views.IndexView, name='index'),
    path('index/web-design', views.WebDesignView, name='web-design'),
    path('index/graphics-design', views.GraphicsDesignView, name='graphics-design'),
    path('index/software-development', views.SoftwareDevelopmentView, name='software-development'),
    path('index/web-design/home', views.IndexView, name="back-to-home"),
    path('index/web-design/services', views.IndexView, name="back-to-home"),
    path('index/ContactForm', views.ContactFormView, name="ContactForm"),
    
    

    



]










