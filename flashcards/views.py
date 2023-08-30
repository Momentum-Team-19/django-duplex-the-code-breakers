# views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Deck, Card
from .forms import DeckForm, CardForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.
def homepage(request):
    return render(request, "index.html")


@login_required
def create_deck(request):
    if request.method == 'POST':
        form = DeckForm(request.POST)
        if form.is_valid():
            deck = form.save(commit=False)
            deck.user = request.user
            deck.save()
            return redirect('homepage')
    else:
        form = DeckForm()
    return render(request, "create_deck.html", {'form': form})


@login_required
def create_card(request):
    if request.method == 'POST':
        form = CardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = CardForm()
    return render(request, "create_card.html", {'form': form})


@login_required
def decks_list(request):
    decks = Deck.objects.filter(user=request.user)
    user = request.user
    context = {
        'decks': decks,
        'user': user,
    }
    return render(request, 'view_decks.html', context)


@login_required
def deck_details(request, pk):
    deck = get_object_or_404(Deck, pk=pk)
    user = request.user
    context = {
        'deck': deck,
        'user': user,
    }

    return render(request, 'deck_details.html', context)


@login_required
def cards_list(request, pk):
    deck = get_object_or_404(Deck, pk=pk)
    cards = Card.objects.all()

    return render(request, 'view_cards.html', {'cards': cards})


@login_required
def card_details(request, pk):
    card = get_object_or_404(Card, pk=pk)

    return render(request, 'card_details.html', {'card': card})