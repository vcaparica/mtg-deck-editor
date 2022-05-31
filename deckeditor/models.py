from django.db import models

class Deck (models.Model):
    name = models.CharField('Deck Name', max_length = 100)
    format = models.CharField('Format', max_length = 50)
    main_cards = models.CharField('Main Deck', max_length = 10000)
    side_cards = models.CharField('Sideboard', max_length = 10000)
    commander = models.CharField('Commander', max_length = 50)


class Card (models.Model):
    oracle_id = models.CharField('Oracle ID', max_length = 36)
    back_name = models.CharField('Back', blank=True, max_length = 100)
    name = models.CharField('Name', max_length = 100)
    mana_cost = models.CharField('Mana Cost', blank=True, max_length = 50)
    cmc = models.CharField('MV', max_length = 2)
    colors = models.CharField('Colors', blank=True, max_length = 15)
    color_identity = models.CharField('Identity', blank=True, max_length = 15)
    art_crop = models.CharField('Art', blank=True, max_length = 200)
    type_line = models.CharField('Type', max_length = 100)
    set = models.CharField('Set', max_length = 5)
    set_name = models.CharField('Set', max_length = 50)
    keywords = models.CharField('Keywords', max_length = 250)
    legalities = models.CharField('Legalities', max_length = 250)
    oracle_text = models.CharField('Oracle', blank=True, max_length = 1000)
    flavor_text = models.CharField('Flavor', blank=True, max_length = 1000)
    artist = models.CharField('Artist', blank=True, max_length = 50)
    power = models.CharField('Power', blank=True, max_length = 3)
    toughness = models.CharField('Toughness', blank=True, max_length = 3)
    rarity = models.CharField('Rarity', max_length = 1)

    def __str__ (self):
        cardstring = f"{self.name}. {self.mana_cost}, {self.type_line}, {self.rarity}, self.set"
        return cardstring

    def general_id(self):
        card = Card.objects.get(name=self.name)
        return card.id