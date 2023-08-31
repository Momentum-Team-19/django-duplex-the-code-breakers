# views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Deck, Card
from .forms import DeckForm, CardForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from random import shuffle
import random as rand


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
            return redirect('list_decks')
    else:
        form = DeckForm()
    return render(request, "edit_deck.html", {'form': form})


@login_required
def edit_deck(request, pk):
    deck = get_object_or_404(Deck, pk=pk)

    if request.method == 'POST':
        form = DeckForm(request.POST, instance=deck)
        if form.is_valid():
            form.save()
            return redirect('deck_details', pk=deck.pk)
    else:
        form = DeckForm(instance=deck)

    context = {
        'form': form,
        'deck': deck,
    }

    return render(request, 'edit_deck.html', context)


@login_required
def create_card(request, pk):
    deck = get_object_or_404(Deck, pk=pk)
    if request.method == 'POST':
        form = CardForm(request.POST)
        if form.is_valid():
            card = form.save(commit=False)
            card.deck = deck
            card.save()
            return redirect('deck_details', pk=deck.pk)
    else:
        form = CardForm()

    context = {
        'form': form,
        'deck': deck,
    }
    return render(request, "edit_card.html", context)


@login_required
def edit_card(request, pk):
    card = get_object_or_404(Card, pk=pk)
    deck_id = card.deck_id

    if request.method == 'POST':
        form = CardForm(request.POST, instance=card)
        if form.is_valid():
            form.save()
            return redirect('deck_details', pk=deck_id)
    else:
        form = CardForm(instance=card)

    context = {
        'form': form,
        'card': card,
        'pk': deck_id,
    }
    
    return render(request, 'edit_card.html', context)


@login_required
def decks_list(request):
    decks = Deck.objects.filter(user=request.user)
    user = request.user

    if decks.exists():
        context = {
            'decks': decks,
            'user': user,
        }
        return render(request, 'decks_list.html', context)
    else:
        message = "No decks :("
        context = {
            'message': message,
            'user': user,
        }
        return render(request, 'decks_list.html', context)


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
    cards = Card.objects.filter(deck=deck)

    if cards.exists():
        context = {
            'cards': cards,
            'deck': deck,
        }
        return render(request, 'cards_list.html', context)
    else:
        message = "No cards :("
        context = {
            'message': message,
            'deck': deck,
        }
        return render(request, 'cards_list.html', context)


@login_required
def card_details(request, pk):
    card = get_object_or_404(Card, pk=pk)
    deck_id = card.deck_id

    context = {
        'card': card,
        'deck_id': deck_id,
    }

    return render(request, 'card_details.html', context)


@login_required
def delete_deck(request, pk):
    deck = get_object_or_404(Deck, pk=pk)
    obj = 'deck'

    if request.method == 'POST':
        deck.delete()
        return redirect('list_decks')

    context = {
        'deck': deck,
        'obj': obj,
    }

    return render(request, 'confirm_delete.html', context)


@login_required
def delete_card(request, pk):
    card = get_object_or_404(Card, pk=pk)
    deck_id = card.deck_id
    obj = 'card'

    if request.method == 'POST':
        card.delete()
        return redirect('list_cards', pk=deck_id)

    context = {
        'card': card,
        'obj': obj,
    }

    return render(request, 'confirm_delete.html', context)


@login_required
def study(request, pk):
    deck = get_object_or_404(Deck, pk=pk)
    cards = list(Card.objects.filter(deck=deck)) # <= add filter for 'card.correct = False'

    shuffle(cards)

    card = rand.choice(cards)

    if card.correct is True:
        pass

    # need 2 buttons, if 'correct' button pressed, => mark card (correct = True), if 'not true' is pressed, => refresh
    # card.save(correct = True)

    shuffled_cards.remove(card)

    context = {
        'card': card,
        'cards': cards,
        'deck': deck,
    }

    print(shuffled_cards)
    print(f'selected card is: {card}')

    return render(request, 'study.html', context)
