from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View

from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework.response import Response
import numpy as np
import pandas as pd


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
dataset = df.values.tolist()

class TableData(APIView):

    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        columns = list(dataset[0])
        pokemon = list(dataset[1])
        data = {
            "columns": columns,
            "data": pokemon,
        }
        print data['pokemon']
        return JsonResponse(data)
