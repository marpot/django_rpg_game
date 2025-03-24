from django.db import models
from adventures.models import Adventure, Location
from accounts.characters.models import PlayerCharacter

class GameSession(models.Model):
    player = models.ForeignKey(PlayerCharacter, on_delete=models.CASCADE, related_name="sessions")
    progress = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.player.name} - {self.player.adventure.title} (Session)"
    
class GameEvent(models.Model):
    EVENT_TYPES = [
        ('story', 'Historia'),
        ('choice', 'Wybór'),
        ('combat', 'Walka'),
        ('item', 'Przedmiot'),
        ('status', 'Status'),
        ('quest', 'Zadanie'),
        ('shop', 'Sklep'),
        ('treasure', 'Skarb'),
    ]

    # Podstawowe pola
    adventure = models.ForeignKey(Adventure, on_delete=models.CASCADE, related_name="game_events")
    player = models.ForeignKey(PlayerCharacter, on_delete=models.CASCADE, related_name="game_events")
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True, related_name="game_events")
    description = models.TextField()
    event_type = models.CharField(max_length=20, choices=EVENT_TYPES, default='story')
    timestamp = models.DateTimeField(auto_now_add=True)

    # Wymagania i flagi
    required_flags = models.JSONField(default=list, blank=True)  # Flagi wymagane do aktywacji zdarzenia
    blocking_flags = models.JSONField(default=list, blank=True)  # Flagi blokujące zdarzenie
    requirements = models.JSONField(default=dict, blank=True)  # Wymagania do aktywacji zdarzenia (poziom, przedmioty, umiejętności)

    # Dane zdarzenia i wybory
    event_data = models.JSONField(default=dict, blank=True)  # Specyficzne dane dla typu zdarzenia
    choices = models.JSONField(default=list, blank=True)  # Lista dostępnych wyborów
    consequences = models.JSONField(default=dict, blank=True)  # Konsekwencje wyborów

    def __str__(self):
        return f"{self.player.name} - {self.description} ({self.timestamp})"

    def is_available(self, player):
        """
        Sprawdza czy zdarzenie jest dostępne dla gracza
        """
        # Sprawdź wymagane flagi
        for flag in self.required_flags:
            if flag not in player.flags:
                return False

        # Sprawdź blokujące flagi
        for flag in self.blocking_flags:
            if flag in player.flags:
                return False

        # Sprawdź wymagania
        if self.requirements:
            if player.level < self.requirements.get('min_level', 0):
                return False
            
            for item in self.requirements.get('required_items', []):
                if item not in player.inventory:
                    return False
            
            for skill in self.requirements.get('required_skills', []):
                if skill not in player.skills:
                    return False

        return True

    def get_available_choices(self, player):
        """
        Zwraca listę dostępnych wyborów dla gracza
        """
        available_choices = []
        for choice in self.choices:
            if self._is_choice_available(choice, player):
                available_choices.append(choice)
        return available_choices

    def _is_choice_available(self, choice, player):
        """
        Sprawdza czy wybór jest dostępny dla gracza
        """
        requirements = choice.get('requirements', {})
        
        # Sprawdź poziom
        if player.level < requirements.get('min_level', 0):
            return False
        
        # Sprawdź przedmioty
        for item in requirements.get('required_items', []):
            if item not in player.inventory:
                return False
        
        # Sprawdź umiejętności
        for skill in requirements.get('required_skills', []):
            if skill not in player.skills:
                return False
        
        # Sprawdź flagi
        for flag in requirements.get('required_flags', []):
            if flag not in player.flags:
                return False
        
        return True
