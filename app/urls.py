from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('rooms/', views.rooms),
    path('room/<int:id>/', views.room),
    path('create-room/', views.createroom),
    path('update-room/<int:id>', views.updateroom),
]