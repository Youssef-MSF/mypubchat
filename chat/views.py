# chat/views.py
from django.shortcuts import render, redirect
from .models import Message


def index(request):
    return render(request, 'chat/index.html', {})


def room(request):
    try:
        # Get all the public messages
        messages = Message.objects.all()

        return render(request, 'chat/chatroom.html', {'username': request.session['username'], 'messages': messages})
    except:
        return redirect('/')


def login(request):
    username = request.POST['name']

    print(username)

    if username == "":
        return render(request, 'chat/index.html')
    else:
        request.session['username'] = username
        return redirect('/chatroom')
