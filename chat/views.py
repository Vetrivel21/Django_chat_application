from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import chat, chatroom

class index(View):
	def get(self, request):
		return render(request, 'chat/index.html')

class room(View):
	def get(self, request, room_name):
		room = chatroom.objects.filter(name=room_name).first()
		chats = []

		if room:
			chats = chat.objects.filter(room=room)
		else:
			room = chatroom(name=room_name)
			room.save()

		return render(request, 'chat/room.html', {'room_name': room_name, 'chats': chats})
