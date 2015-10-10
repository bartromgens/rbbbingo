import logging
logger = logging.getLogger(__name__)

from django.views.generic import TemplateView

from bingo.models import get_random_field_value
from bingo.models import add_info_to_card
from bingo.models import Card
from bingo.models import Field
from bingo.models import FieldValue


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
