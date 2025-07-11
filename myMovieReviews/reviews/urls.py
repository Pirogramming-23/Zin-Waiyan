##reviews

from django.urls import path
from .views import *

urlpatterns = [
    path("",reviews_list),
    path("<int:pk>/",reviews_detail),
    path("create/",reviews_create),
    path("<int:pk>/delete/",reviews_delete),
    path("<int:pk>/update/",reviews_update),
]