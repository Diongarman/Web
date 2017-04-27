from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse, HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
import pandas as pd

#json formatting
import json

#File Paths
from settings import BASE_DIR

#GLOBALS
pokemon_csv = BASE_DIR + '/pokemon-sun-and-moon-gen-7-stats/pokemon.csv'

#HomeView contains ajax api calls to TableData and PokemonChartData
class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'charts.html')


class TableData(APIView):

    authentication_classes = []
    permission_classes = []



    def get(self, request, format=None):
        df = pd.read_csv(pokemon_csv, header=None).fillna('N/A').values.tolist()

        header = list(map(lambda col: {'title': col}, df[0]))
        pokemon = json.dumps(df[1:])

        data = {
            "data": pokemon,
            "columns": header
        }


        return Response(data)

class PokemonChartData(APIView):
    #structure and format data for charts.js to display, aggregate, group etc.

    def get(self, request, format=None):
        df2 = pd.read_csv(pokemon_csv)

        type_counts = df2['type1'].value_counts().tolist()
        types = df2['type1'].value_counts().index.tolist()

        type2_counts = df2['type2'].value_counts().tolist()
        types2 = df2['type2'].value_counts().index.tolist()

        data = {
            "types": types,
            "type_counts": type_counts,
            "types2": types2,
            "type2_counts": type2_counts
        }


        return Response(data)


