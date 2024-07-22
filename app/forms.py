from django.forms import ModelForm
from .models import Room, User
from django.contrib.auth.forms import UserCreationForm


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host', 'participants']


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'username', 'name', 'bio']
