from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('rooms/', views.rooms),
    path('room/<int:id>/', views.room),
    path('create-room/', views.createroom),
    path('update-room/<int:id>', views.updateroom),
    path('delete-room/<int:id>', views.deleteroom),
    path('delete_message/<int:id>', views.deletemessage),
    path('login/', views.loginpage),
    path('logout/', views.logoutpage),
    path('create_account/', views.create_account),
    path('profile/<int:id>', views.userprofile),
]