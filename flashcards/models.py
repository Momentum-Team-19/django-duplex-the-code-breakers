# models.py
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    pass


class Deck(models.Model):
    title = models.CharField(max_length=200)
    desc = models.CharField(max_length=200, blank=True, null=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="decks")
    created_date = models.DateTimeField(default=timezone.now)

    def archive(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Card(models.Model):
    deck = models.ForeignKey(
        Deck, on_delete=models.CASCADE, related_name="cards")
    prompt = models.CharField(max_length=200)
    hint = models.CharField(max_length=200, blank=True, null=True)
    answer = models.CharField(max_length=200)
    correct = models.BooleanField(default=False)

    def __str__(self):
        return self.prompt

    # def mark_correct(self):
    #     pass
    # 
