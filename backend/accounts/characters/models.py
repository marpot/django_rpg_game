from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class PlayerCharacter(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    level = models.IntegerField(default=1)
    experience = models.IntegerField(default=0)
    health = models.IntegerField(default=100)
    max_health = models.IntegerField(default=100)
    mana = models.IntegerField(default=100)
    max_mana = models.IntegerField(default=100)
    strength = models.IntegerField(default=10)
    dexterity = models.IntegerField(default=10)
    intelligence = models.IntegerField(default=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} (Level {self.level})"

    def gain_experience(self, amount):
        self.experience += amount
        while self.experience >= self.level * 1000:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.experience -= (self.level - 1) * 1000
        self.max_health += 10
        self.max_mana += 10
        self.health = self.max_health
        self.mana = self.max_mana
        self.strength += 2
        self.dexterity += 2
        self.intelligence += 2
        self.save() 