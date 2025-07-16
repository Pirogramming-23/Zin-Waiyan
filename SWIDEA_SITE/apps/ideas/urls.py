#apps.ideas.urls.py

from django.urls import path
from .views import *

app_name = 'ideas'

urlpatterns = [
    path('',main,name='main'),
    path('create',create,name='create'),
    path('detail/<int:pk>',detail,name='detail'),
    path('update/<int:pk>',update,name='update'),
    path('delete/<int:pk>', delete, name='delete'),
    path('toggle_star/<int:pk>/', toggle_star, name='toggle_star'),
    path('adjust_interest/<int:pk>/', adjust_interest, name='adjust_interest'),
]

