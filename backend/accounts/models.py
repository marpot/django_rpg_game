from django.db import models
from adventures.models import Adventure, Location
from accounts.users.models import CustomUser

class PlayerProfile(models.Model):
	user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
	level = models.IntegerField(default=1)

	def __str__(self):
		return f"{self.user.username} - Level {self.level}"

class PlayerCharacter(models.Model):
	user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="characters")
	adventure = models.ForeignKey(Adventure, on_delete=models.CASCADE, related_name="players")
	name = models.CharField(max_length=100)
	current_location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True)
	
	level = models.IntegerField(default=1)
	experience = models.IntegerField(default=0)
	health = models.IntegerField(default=100)
	max_health = models.IntegerField(default=100)
	mana = models.IntegerField(default=50)
	max_mana = models.IntegerField(default=50)
	
	strength = models.IntegerField(default=10)
	dexterity = models.IntegerField(default=10)
	intelligence = models.IntegerField(default=10)
	constitution = models.IntegerField(default=10)
	wisdom = models.IntegerField(default=10)
	charisma = models.IntegerField(default=10)
	
	equipment = models.JSONField(default=dict)
	inventory = models.JSONField(default=list)
	skills = models.JSONField(default=list)
	status_effects = models.JSONField(default=list)
	progress = models.JSONField(default=dict)
	
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	is_active = models.BooleanField(default=True)

	def __str__(self):
		return f"{self.name} (Poziom {self.level}) - {self.adventure.title}"
	
	def add_experience(self, amount):
		self.experience += amount
		new_level = (self.experience // 1000) + 1
		if new_level > self.level:
			self.level_up(new_level)
		self.save()
	
	def level_up(self, new_level):
		self.level = new_level
		self.max_health += 10
		self.health = self.max_health
		self.max_mana += 5
		self.mana = self.max_mana
	
	def add_item(self, item):
		self.inventory.append(item)
		self.save()
	
	def remove_item(self, item_id):
		self.inventory = [item for item in self.inventory if item['id'] != item_id]
		self.save()
	
	def add_status_effect(self, effect):
		self.status_effects.append(effect)
		self.save()
	
	def remove_status_effect(self, effect_id):
		self.status_effects = [effect for effect in self.status_effects if effect['id'] != effect_id]
		self.save()
	
	def update_progress(self, key, value):
		self.progress[key] = value
		self.save()