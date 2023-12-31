# forms.py

from django import forms
from .models import Deck, Card


class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ['prompt', 'hint', 'answer']


class DeckForm(forms.ModelForm):
    class Meta:
        model = Deck
        fields = ['title', 'desc']
