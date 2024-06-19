from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from .models import Room
from .forms import RoomForm

# contact = [
#     {'id': 1, 'name': 'lets learn python'},
#     {'id': 2, 'name': 'lets learn JS'},
#     {'id': 3, 'name': 'lets learn C++'},
# ]


def home(request):
    return render(request, 'home.html')

def rooms(request):
    contact = Room.objects.all()
    return render(request, 'rooms.html', {'rooms': contact})

def room(request, id):
    # r = None
    # for i in contact:
    #     if i['id'] == int(id):
    #         r = i
    r = Room.objects.filter(id=id).first()

    return render(request, 'room.html', {'room': r})

def createroom(request):
    form = RoomForm()
    if request.method == 'POST':
        f = RoomForm(request.POST)
        if f.is_valid():
            f.save()
            return redirect('/rooms')
    return render(request, 'room_form.html', {'form': form})

def updateroom(request, id):
    room = Room.objects.filter(id=id).first()
    if not room:
        return render(request, 'room.html', {'room': None})
    form = RoomForm(instance=room)
    if request.method == 'POST':
        f = RoomForm(request.POST, instance=room)
        if f.is_valid():
            f.save()
            return redirect('/rooms')
    return render(request, 'room_form.html', {'form': form})