from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('rooms/', views.rooms),
    path('room/<int:id>/', views.room, name='room'),
    path('create-room/', views.createroom),
    path('update-room/<int:id>', views.updateroom),
    path('delete-room/<int:id>', views.deleteroom),
    path('delete_message/<int:id>', views.deletemessage),
    path('login/', views.loginpage),
    path('logout/', views.logoutpage),
    path('create_account/', views.create_account),
    path('profile/<int:id>', views.userprofile),
    path('update-profile/<int:id>', views.updateprofile),
    # path('chat/<str:room_name>/', views.room_test, name='room_test'),
    path('room_messages/<int:id>/', views.room_messages, name='room_messages'),
]