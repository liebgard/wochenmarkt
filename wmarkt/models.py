from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Rezept(models.Model):
    name = models.CharField(max_length=120)
    beschreibung = models.TextField()
    anleitung = models.TextField()
    datum_erschienen = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

