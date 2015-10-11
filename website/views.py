import logging
logger = logging.getLogger(__name__)

from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.conf import settings
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.views.generic import FormView

from registration.views import RegistrationView
from registration import signals

from bingo.models import add_info_to_card
from bingo.models import add_info_to_game
from bingo.models import create_card
from bingo.models import Card
from bingo.models import Field
from bingo.models import FieldValue
from bingo.models import Game

from bingo.forms import NewFieldValuedForm
from bingo.forms import NewGameForm


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
        games = Game.objects.all()
        for game in games:
            add_info_to_game(game)
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
        context = super(CheckFieldView, self).get_context_data(**kwargs)
        field = Field.objects.get(id=field_id)
        if field.card.user != self.request.user:  # users can only change fields on their own cards
            return context
        field.is_checked = not field.is_checked
        field.save()
        return context


class JoinGameView(TemplateView):
    template_name = "website/joingame.html"
    context_object_name = "join_game"

    def get_context_data(self, game_id, **kwargs):
        context = super(JoinGameView, self).get_context_data(**kwargs)
        game = Game.objects.get(id=game_id)
        has_events = FieldValue.objects.count()
        if not has_events:
            context['message'] = "There are no events to use in a new game card. Please create some events first."
        elif Card.objects.filter(user=self.request.user, game=game):
            context['message'] = "You are already participating in this game!"
        else:
            create_card(game, self.request.user)
            context['message'] = "New bingo card created for you!"
        return context


class NewEventView(FormView):
    template_name = 'website/event_new.html'
    form_class = NewFieldValuedForm
    success_url = '/events/'

    def form_valid(self, form):
        super(NewEventView, self).form_valid(form)
        form.save()
        return HttpResponseRedirect('/events/')

    def get_context_data(self, **kwargs):
        context = super(NewEventView, self).get_context_data(**kwargs)
        return context


class NewGameView(FormView):
    template_name = 'website/game_new.html'
    form_class = NewGameForm
    success_url = '/games/'

    def form_valid(self, form):
        super(NewGameView, self).form_valid(form)
        form.save()
        return HttpResponseRedirect('/games/')

    def get_context_data(self, **kwargs):
        context = super(NewGameView, self).get_context_data(**kwargs)
        return context


class RBBingoNewRegistrationView(RegistrationView):
    success_url = '/'

    def register(self, request, form):
        new_user = form.save()
        username_field = getattr(new_user, 'USERNAME_FIELD', 'username')
        new_user = authenticate(
            username=getattr(new_user, username_field),
            password=form.cleaned_data['password1']
        )

        login(request, new_user)
        signals.user_registered.send(sender=self.__class__,
                                     user=new_user,
                                     request=request)
        return new_user

    def registration_allowed(self, request):
        """
        Indicate whether account registration is currently permitted,
        based on the value of the setting ``REGISTRATION_OPEN``. This
        is determined as follows:

        * If ``REGISTRATION_OPEN`` is not specified in settings, or is
          set to ``True``, registration is permitted.

        * If ``REGISTRATION_OPEN`` is both specified and set to
          ``False``, registration is not permitted.

        """
        return getattr(settings, 'REGISTRATION_OPEN', True)
