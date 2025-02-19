from django.db import models # type: ignore
from django.contrib.auth.models import User # type: ignore

class Adventure(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="adventures")

    def __str__(self):
        return self.title

class Location(models.Model):
    adventure = models.ForeignKey(Adventure, on_delete=models.CASCADE, related_name="locations")
    title = models.CharField(max_length=255)
    description = models.TextField()
    def __str__(self):
        return f"{self.adventure.title} - {self.title}"
    
    class Meta:
        verbose_name_plural = "locations"

class Choice(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="choices")
    title = models.CharField(max_length=255)
    description = models.TextField()
    next_location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True, related_name="choices_leading_here")
    effects = models.JSONField(null=True, blank=True)

    def __str__(self):
        return f"{self.location.adventure.title} - {self.location.title} - {self.title}"