from django.contrib import admin
from .models import Room, Message

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('user', 'room', 'timestamp', 'is_flagged') # On garde is_flagged pour Becker
    list_filter = ('is_flagged', 'room', 'timestamp')
    search_fields = ('content', 'user__username')
