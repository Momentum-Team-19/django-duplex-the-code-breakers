from django.db import models
from django.utils import timezone
from django.contib.auth.models import AbstractUser

# Create your models here.


class Deck(models.Model):
    title = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    pass


class Card(models.Model):
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE, related_name="decks")
    prompt = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)
    pass


class User(AbstractUser):
    pass

