from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from .models import Room, Topic
from .forms import RoomForm
from django.db.models import Q

# contact = [
#     {'id': 1, 'name': 'lets learn python'},
#     {'id': 2, 'name': 'lets learn JS'},
#     {'id': 3, 'name': 'lets learn C++'},
# ]


def home(request):
    return render(request, 'home.html')

def rooms(request):
    q = request.GET.get('q')
    if q:
        # contains for search for any one contains these latters!
        contact = Room.objects.filter(
            Q(topic__name__contains=q) |
            Q(name__contains=q) |
            Q(description__contains=q)
        )
        if not contact:
            return render(request, 'room.html', {'room': None})
    else:
        contact = Room.objects.all()
    rooms_count = contact.count()
    topics = Topic.objects.all()
    return render(request, 'rooms.html', {'rooms': contact, 'topics': topics, 'rooms_count': rooms_count})

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

def deleteroom(request, id):
    room = Room.objects.filter(id=id).first()
    if not room:
        return render(request, 'room.html', {'room': None})
    if request.method == 'POST':
        room.delete()
        return redirect('/rooms')
    return render(request, 'delete.html', {'room': room})