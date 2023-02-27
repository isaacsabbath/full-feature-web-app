from django.urls import path
from . import views

urlpatterns = [     #the homepage
    path('', views.home, name='blog-home'), 
]          
 # (blog-home)- used to do reverse lookup on the route and could collide with other names