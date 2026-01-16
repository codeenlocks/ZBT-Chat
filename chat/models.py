from django.db import models
from django.contrib.auth.models import User

# Partie de Zainab (Les Salons)
class Room(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

# Partie de Hermès (Les Messages) + celle de Becker (Modération)
class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="messages")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    # Pour la modération de Becker
    is_flagged = models.BooleanField(default=False) 

    class Meta:
        ordering = ['timestamp']