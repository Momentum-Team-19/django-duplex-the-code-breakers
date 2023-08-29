from django.db import models
from django.utils import timezone
from django.contib.auth.models import AbstractUser

# Create your models here.


class Deck(models.Model):
    title = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)

    def archive(self):
        self.created_date = timezone.now()
        self.save()
    
    def __str__(self):
        return self.title


class Card(models.Model):
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE, related_name="decks")
    prompt = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)
    
    def __str__(self):
        return self.prompt
        


class User(AbstractUser):
    pass
