from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
	groups = models.ManyToManyField(
		'auth.Group',
		related_name='customuser_set',
		blank=True,
		help_text='The groups this user belongs to.',
		related_query_name='customuser'
		)
	user_permissions = models.ManyToManyField(
		'auth.Permission',
		related_name='customuser_set',
		blank=True,
		help_text='Specific permissions for this user',
		related_query_name='customuser'
		)

class PlayerProfile(models.Model):
	user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
	level = models.IntegerField(default=1)

	def __str__(self):
		return f"{self.user.username} - Level {self.level}"