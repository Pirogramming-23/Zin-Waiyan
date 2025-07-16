#apps.tools.urls.py

from django.urls import path
from .views import *

app_name = 'tools'

urlpatterns = [
    path('tools_list',tools_list,name='tools_list'),
    path('create',create,name='create'),
    path('detail/<int:pk>',detail,name='detail'),
    path('update/<int:pk>',update,name='update'),
    path('delete/<int:pk>', delete, name='delete'),
]
