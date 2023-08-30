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

    return render(request, 'edit_deck.html', {'form': form})


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
    return render(request, "edit_card.html", {'form': form})


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

    return render(request, 'edit_card.html', {'form': form})


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
def delete_card(request, pk):
    card = get_object_or_404(Card, pk=pk)
    deck_id = card.deck_id

    if request.method == 'POST':
        card.delete()
        return redirect('list_cards', pk=deck_id)
    return render(request, 'confirm_delete.html', {'card': card})


@login_required
def delete_deck(request, pk):
    deck = get_object_or_404(Deck, pk=pk)

    if request.method == 'POST':
        deck.delete()
        return redirect('list_decks')
    return render(request, 'confirm_delete.html', {'deck': deck})
