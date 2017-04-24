from django.contrib.auth import get_user_model
from django.http import JsonResponse
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
        return render(request, 'charts.html', {"sales": 25, "customers": 19})


def get_data(request, *args,**kwargs):
    data = {
        "sales": 100,
        "customers": 10
    }
    return JsonResponse(data)

#all three have some result, this is the best way though
class ChartData(APIView):

    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        user_count = User.objects.all().count()
        labels = ["Users", "Blue", "Yellow", "Green", "Purple", "Orange"]
        default_items = [user_count, 14,11,12, 2, 9]
        data = {
            "labels": labels,
            "default": default_items,
            "users": User.objects.all().count()
        }
        return Response(data)

df = pd.read_csv('/Users/diongarman/PycharmProjects/Django-Chart.js-9deb1d489250aca706b9939ae0bad331d0709982/src/pokemon-sun-and-moon-gen-7-stats/pokemon.csv', header=None)
dataset = df.fillna('N/A').values.tolist() #fillna() function avoids invalid data being passed by view

class TableData(APIView):

    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        pokemon = dataset[1:3]

        columns = json.dumps(dataset[0])
        pokemon = json.dumps(dataset[1:])


        data = {
            "data": pokemon,
            "columns": columns
        }

        print(type(pokemon))
        print(type(columns))


        return Response(data)
