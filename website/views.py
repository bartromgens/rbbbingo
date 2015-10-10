import logging
logger = logging.getLogger(__name__)

from django.views.generic import TemplateView

from bingo.models import add_info_to_card
from bingo.models import add_info_to_game
from bingo.models import create_card
from bingo.models import Card
from bingo.models import Field
from bingo.models import FieldValue
from bingo.models import Game


class HomeView(TemplateView):
    template_name = "website/index.html"
    context_object_name = "homepage"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        return context


class CardsView(TemplateView):
    template_name = "website/cards.html"
    context_object_name = "cards"

    def get_context_data(self, **kwargs):
        context = super(CardsView, self).get_context_data(**kwargs)
        cards = Card.objects.filter(user=self.request.user)
        for card in cards:
            add_info_to_card(card)
        context['cards'] = cards
        return context


class GamesView(TemplateView):
    template_name = "website/games.html"
    context_object_name = "games"

    def get_context_data(self, **kwargs):
        context = super(GamesView, self).get_context_data(**kwargs)
        cards = Card.objects.filter(user=self.request.user)
        games = []
        for card in cards:
            game = card.game
            add_info_to_game(game)
            games.append(game)
        context['games'] = games
        return context


class EventsView(TemplateView):
    template_name = "website/events.html"
    context_object_name = "events"

    def get_context_data(self, **kwargs):
        context = super(EventsView, self).get_context_data(**kwargs)
        events = FieldValue.objects.all()
        context['events'] = events
        return context


class CheckFieldView(CardsView):

    def get_context_data(self, field_id, **kwargs):
        field = Field.objects.get(id=field_id)
        field.is_checked = not field.is_checked
        field.save()
        context = super(CheckFieldView, self).get_context_data(**kwargs)
        return context


class JoinGameView(TemplateView):
    template_name = "website/joingame.html"
    context_object_name = "join_game"

    def get_context_data(self, game_id, **kwargs):
        context = super(JoinGameView, self).get_context_data(**kwargs)
        game = Game.objects.get(id=game_id)
        if not Card.objects.filter(user=self.request.user, game=game):
            create_card(game, self.request.user)
            context['message'] = "A new bingo card for this game is created for you!"
        else:
            context['message'] = "You are already participating in this game!"
        return context
