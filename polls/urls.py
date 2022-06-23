from django.urls import path

from . import views

urlpatterns = [
    path('icecream/soda', views.index, name = 'index')
]