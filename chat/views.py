# chat/views.py
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Message

# Import smtplib to send mails
import smtplib


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


def send_mail(request):
    # Sender email
    sender_email = "linked.clubs@gmail.com"
    # Receiver email
    receiver_email = request.GET['rec']
    # Message to send
    message = request.GET['message']

    msg = f'subject: LinkedClubs\n\n{message}'

    # Initialize the server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    # Start the server
    server.starttls()

    # Login
    server.login(sender_email, "linkedclubs2020")
    print("Login success !")

    # Send the message
    server.sendmail(sender_email, receiver_email, msg)

    print("Email has been sent successfully !")

    return HttpResponse('<h1>Welcome</h1>')
