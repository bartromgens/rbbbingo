from django.db import models
from django.contrib.auth.models import User

from easy_thumbnails.fields import ThumbnailerImageField


class Game(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Card(models.Model):
    game = models.ForeignKey(Game)
    user = models.ForeignKey(User)

    def __str__(self):
        return "Card for game: " + str(self.game)


class Field(models.Model):
    card = models.ForeignKey(Card)
    field_value = models.ForeignKey("FieldValue", related_name="field_value")
    position = models.IntegerField()
    is_checked = models.BooleanField(default=False, blank=False)


class FieldValue(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000, blank=True)
    image = ThumbnailerImageField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Event"


def get_random_field_value(exclude_field_value_ids):
    value_random = FieldValue.objects.exclude(id__in=exclude_field_value_ids)
    if value_random:
        return value_random.order_by('?').first()
    assert False
    return value_random


def create_card(game, user):
    card = Card()
    card.game = game
    card.user = user
    card.save()
    n_fields = FieldValue.objects.count()
    exclude_field_value_ids = []
    for i in range(1, 26):  # 5x5 field
        field = Field()
        field.card = card
        field.position = i
        if len(exclude_field_value_ids) < n_fields:
            field_value = get_random_field_value(exclude_field_value_ids)
        else:
            field_value = get_random_field_value([])
        exclude_field_value_ids.append(field_value.id)
        field.field_value = field_value
        field.save()


def add_info_to_card(card):
    fields = Field.objects.filter(card=card)
    card.fields = fields


def add_info_to_game(game):
    cards = Card.objects.filter(game=game)
    players = []
    for card in cards:
        players.append(card.user)
    game.players = players
    game.n_players = len(players)
