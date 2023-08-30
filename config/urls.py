# urls.py
"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from flashcards import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.homepage, name="homepage"),
    path("accounts/", include("registration.backends.simple.urls")),
    path('decks/new', views.create_deck, name='create_deck'),
    path('card/new/<int:pk>', views.create_card, name='create_card'),
    path('decks/list', views.decks_list, name='list_decks'),
    path('deck/detail/<int:pk>', views.deck_details, name='deck_details'),
    path('cards/list/<int:pk>', views.cards_list, name='list_cards'),
    path('card/detail/<int:pk>', views.card_details, name='card_details'),
    path('deck/delete/<int:pk>', views.delete_deck, name='deck_delete'),
    path('card/delete/<int:pk>', views.delete_card, name='card_delete'),
]
