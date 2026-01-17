from django.db import models
from django.contrib import admin
from .models import Room, Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    # Affiche une colonne "Signalé" dans la liste des messages 
    list_display = ('user', 'room', 'content', 'timestamp', 'is_flagged')
    # Permet de filtrer pour voir uniquement les messages signalés
    list_filter = ('is_flagged', 'timestamp')
    # Permet au modérateur de "dé-flaguer" ou valider directement
    list_editable = ('is_flagged',)

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)} # Remplit le slug automatiquement

admin.site.register(Message)