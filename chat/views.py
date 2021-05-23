from django.shortcuts import render
from django.shortcuts import redirect


def index(request):
    if request.method == "POST":
        room_name = request.POST.get('room-name')
        room_path = '/chat/'+room_name
        return redirect(room_path)
    return render(request, 'index.html', {})


def room(request, room_name):
    return render(request, 'chatroom.html', {
        'room_name': room_name
    })
