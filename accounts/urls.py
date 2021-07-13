
from django.urls import path, include
from . import views

urlpatterns = [
    path('index/',  views.IndexView.as_view(), name="index"),
    path('index/web-design', views.WebDesignView.as_view(), name='web-design'),
    path('index/graphics-design', views.GraphicsDesignView.as_view(), name='graphics-design'),
    path('index/software-development', views.SoftwareDevelopmentView.as_view(), name='software-development'),
    path('index/web-design/home', views.IndexView.as_view(), name="back-to-home"),
    path('index/web-design/services', views.IndexView.as_view(), name="back-to-home"),
    path('index/ContactForm', views.ContactFormView, name="ContactForm"),
    
    

    



]










