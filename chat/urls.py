# chat/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('chatroom/', views.room, name='chatroom'),
    path('login/', views.login, name='login'),
    path('sendwelcomemail/', views.send_mail, name="send_welcome_mail")
]
