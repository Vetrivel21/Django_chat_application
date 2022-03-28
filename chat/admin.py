from django.contrib import admin

from .models import chat
from .models import chatroom

admin.site.register(chat)
admin.site.register(chatroom)

