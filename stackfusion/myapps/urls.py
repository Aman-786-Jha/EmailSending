from django.urls import path 
from . import views 

urlpatterns = [
    path('',views.index,name='index'),
    path('index/createdata/',views.createdata,name='createdata'),
    path('posts/',views.posts,name='posts'),
    path('home/',views.home,name='home')
    
]
