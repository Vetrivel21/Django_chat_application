from django.urls import path
from .views import index, room

urlpatterns = [
	path('', index.as_view(), name='index'),
	path('<str:room_name>/', room.as_view(), name='room'),
]
