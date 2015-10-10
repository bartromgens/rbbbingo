from django.contrib import admin

from bingo.models import Card
from bingo.models import Field
from bingo.models import FieldValue
from bingo.models import Game


class GameAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
    ]
    list_display = ('name',)


class CardAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['game']}),
        (None, {'fields': ['user']}),
    ]
    list_display = ('game', 'user',)


class FieldAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['card']}),
        (None, {'fields': ['field_value']}),
        (None, {'fields': ['position']}),
        (None, {'fields': ['is_checked']}),
    ]
    list_display = ('card', 'field_value', 'position', 'is_checked')


class FieldValueAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
        (None, {'fields': ['description']}),
        (None, {'fields': ['image']}),
    ]
    list_display = ('name', 'description',)


admin.site.register(Game, GameAdmin)
admin.site.register(Card, CardAdmin)
admin.site.register(Field, FieldAdmin)
admin.site.register(FieldValue, FieldValueAdmin)