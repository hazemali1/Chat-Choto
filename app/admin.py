from django.contrib import admin

# Register your models here.

from .models import Room, Topic, Message

admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)

# obj = Room(name='lets learn how to add data to database', description='this is a test for adding to database with mysql')
# obj.save()
