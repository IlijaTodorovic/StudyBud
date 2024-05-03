from django.shortcuts import render
from .models import Room

#rooms= [
 #   {'id': 1, 'name': 'Lets learn python'},
   # {'id': 2, 'name': 'Design with me'},
  #  {'id': 3, 'name': 'Frontend developers'}
#]

def home(request):
    rooms = Room .objects.all()
    context= {'rooms' : rooms}
    return render(request, 'base/home.html', context)

def room(requset, pk):
    room = Room.objects.get(id=pk)
    context={'room' : room}
    return render(requset, 'base/room.html', context)

# Create your views here.
