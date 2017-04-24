import csv

r = csv.reader(open('/Users/diongarman/PycharmProjects/Django-Chart.js-9deb1d489250aca706b9939ae0bad331d0709982/src/pokemon-sun-and-moon-gen-7-stats/pokemon.csv'))

for x in r:
    for y in x:
        print y
