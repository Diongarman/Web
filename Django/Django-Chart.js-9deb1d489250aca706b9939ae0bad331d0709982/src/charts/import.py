import sys, os, csv

project_dir = "/Users/diongarman/PycharmProjects/Django-Chart.js-9deb1d489250aca706b9939ae0bad331d0709982/src/"

sys.path.append(project_dir)

os.environ['DJANGO_SETTINGS_MODULE'] = 'charts/settings'

import django

#django.setup()

from . import models
from models import Pokemon

data = csv.reader(open(project_dir + "pokemon-sun-and-moon-gen-7-stats/pokemon.csv"), delimiter=",")

for row in data:
    if row[0] != "id":
        pokemon = Pokemon()
        pokemon.id = row[0]
        pokemon.ndex = row[1]
        pokemon.species = row[2]
        pokemon.form = row[3]
        pokemon.type1 = row[4]
        pokemon.type2 = row[5]
        pokemon.ability1 = row[6]
        pokemon.ability2 = row[7]
        pokemon.abilityH = row[8]
        pokemon.hp = row[9]
        pokemon.attack = row[10]
        pokemon.defense = row[11]
        pokemon.spattack = row[12]
        pokemon.spdefense = row[13]
        pokemon.speed = row[14]
        pokemon.total = row[15]
        pokemon.weight = row[16]
        pokemon.height = row[17]
        pokemon.dex1 = row[18]
        pokemon.dex2 = row[19]
        pokemon.class_ = row[20]
        pokemon.percent_male = row[21]
        pokemon.percent_female = row[22]
        pokemon.pre_evolution = row[23]
        pokemon.egg_group1 = row[24]
        pokemon.egg_group2 = row[25]

        pokemon.save()



