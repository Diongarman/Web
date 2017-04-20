from __future__ import unicode_literals
from django.db import models

class Pokemon(models.Model):
    id = models.IntegerField()
    ndex = models.IntegerField()
    species = models.CharField()
    form = models.CharField()
    type1 = models.CharField()
    type2 = models.CharField()
    ability1 = models.CharField()
    ability2 = models.CharField()
    abilityH = models.CharField()
    hp = models.IntegerField()
    attack = models.IntegerField()
    defense = models.IntegerField()
    spattack = models.IntegerField()
    spdefense = models.IntegerField()
    speed = models.IntegerField()
    total = models.IntegerField()
    weight = models.FloatField
    height = models.FloatField
    dex1 = models.CharField()
    dex2 = models.CharField()
    class_ = models.CharField()
    percent_male = models.FloatField()
    percent_female = models.FloatField()
    pre_evolution = models.CharField()
    egg_group1 = models.CharField()
    egg_group2 = models.CharField()
