from django.db import models
from django.contrib import admin
from .models import Room, Message

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)} # Remplit le slug automatiquement

admin.site.register(Message)