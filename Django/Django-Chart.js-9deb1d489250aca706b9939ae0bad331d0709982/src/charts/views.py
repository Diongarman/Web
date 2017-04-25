from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.views.generic import View

from django.http import JsonResponse, HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
import numpy as np
import pandas as pd

#json formatting
import json

User = get_user_model()



class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'charts.html')


df = pd.read_csv('/Users/diongarman/PycharmProjects/Django-Chart.js-9deb1d489250aca706b9939ae0bad331d0709982/src/pokemon-sun-and-moon-gen-7-stats/pokemon.csv', header=None)
dataset = df.fillna('N/A').values.tolist() #fillna() function avoids invalid data being passed by view

class TableData(APIView):

    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        columns = json.dumps(dataset[0])
        pokemon = json.dumps(dataset[1:])

        data = {
            "data": pokemon,
            "columns": columns
        }


        return Response(data)

class PokemonChartData(APIView):
    #structure and format data for charts.js to display, aggregate, group etc.

    def get(self, request, format=None):
        df2 = pd.read_csv(
            '/Users/diongarman/PycharmProjects/Django-Chart.js-9deb1d489250aca706b9939ae0bad331d0709982/src/pokemon-sun-and-moon-gen-7-stats/pokemon.csv')

        type_counts = df2['type1'].value_counts().tolist()
        types = df2['type1'].value_counts().index.tolist()

        data = {
            "types": types,
            "type_counts": type_counts
        }

        return Response(data)


