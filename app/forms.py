from django.forms import ModelForm
from .models import Room, User, Message
from django.contrib.auth.forms import UserCreationForm
from django import forms


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host', 'participants']






class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'username', 'name', 'bio', 'avatar']

    def __init__(self, *args, **kwargs):
        self.user_instance = kwargs.get('instance')
        super(UserForm, self).__init__(*args, **kwargs)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if self.user_instance and self.user_instance.username == username:
            return username  # Return the same username if it hasn't changed
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("A user with that username already exists.")
        return username


class FileForm(ModelForm):
    class Meta:
        model = Message
        fields = ('file', 'body',)
        widgets = {
            'body': forms.TextInput(attrs={'id': 'message-input', 'placeholder': 'Write your message here...'}),
        }

