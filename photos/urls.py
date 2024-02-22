from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.gallery, name='gallery'),
    path("photo/<str:pk>", views.viewPhoto, name='photo'),
    path("add/", views.addPhoto, name='add'),

]
