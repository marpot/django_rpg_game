from django.db import models
from adventures.models import Adventure, Location
from django.conf import settings

class PlayerCharacter(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="characters")
    adventure = models.ForeignKey(Adventure, on_delete=models.CASCADE, related_name="players")
    name = models.CharField(max_length=100)
    current_location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True)
    stats = models.JSONField(default=dict)

    def __str__(self):
        return f"{self.username} - {self.name} ({self.adventure.title})"
    
class GameSession(models.Model):
    player = models.ForeignKey(PlayerCharacter, on_delete=models.CASCADE, related_name="sessions")
    progress = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.player.name} - {self.player.adventure.title} (Session)"
    
class GameEvent(models.Model):
    adventure = models.ForeignKey(Adventure, on_delete=models.CASCADE, related_name="game_events")
    player = models.ForeignKey(PlayerCharacter, on_delete=models.CASCADE, related_name="game_events")
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True, related_name="game_events")
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.player.name} - {self.description} ({self.timestamp})"
