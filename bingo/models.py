from django.db import models
from django.contrib.auth.models import User


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
    image = models.ImageField(blank=True)


def get_random_field_value():
    value_random = FieldValue.objects.order_by('?').first()
    assert value_random
    return value_random


def create_card(game, user):
    card = Card()
    card.game = game
    card.user = user
    for i in range(1, 25):
        field = Field()
        field.card = card
        field.position = i
        field.field_value = get_random_field_value()
        field.save()
    card.save()
