from django.urls import path
from . import views

urlpatterns = [
    path('',views.post_list,name='post_list'), #if someone enter the website at 'http://127.0.0.1:8000/' address, will go to views.post_list   
    path('post/<int:pk>/',views.post_detail,name='post_detail'),
    path('post/new/',views.post_new,name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]