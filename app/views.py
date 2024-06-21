from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from .models import Room, Topic, Message
from .forms import RoomForm
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

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
    if request.method =='POST':
        message = Message.objects.create(
            user=request.user,
            room=r,
            body=request.POST.get('body')
        )
        url = '/room/' + str(r.id)
        return redirect(url)
    room_messages = r.message_set.all().order_by('-created')

    return render(request, 'room.html', {'room': r, 'room_messages': room_messages})

@login_required(login_url='/login')
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

def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        error = False
        try:
            user = User.objects.get(username=username)
        except:
            error = True
            messages.error(request, 'User Does Not Exist!!')

        if not error:
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('/rooms')
            else:
                messages.error(request, 'PassWord is incorrect')
    return render(request, 'login.html')

def logoutpage(request):
    logout(request)
    return redirect('/rooms')

def create_account(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request,user)
            return redirect('/rooms')
        else:
            messages.error(request, 'AnError happend during creating a new account')
    return render(request, 'create_account.html', {'form': form})

