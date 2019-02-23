
from django.urls import path

from . import views

urlpatterns = [
    path('asd/<x>/<y>', views.index, name='index'),
   # path('creatdb/<Name>', views.creatsdb, name='creatsdb'),
    path('dsa', views.Hello, name='hello'),
]
