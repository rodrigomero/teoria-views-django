from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Musician
from django.forms.models import model_to_dict
# Create your views here.

class HelloView(APIView):
    def get(self, request):
        return Response('Hello Kenzie')

class MusicianView(APIView):
    def get(self, request):
        musicians = Musician.objects.all()
        # musicians_dict = []
        # for musician in musicians:
        #     m = model_to_dict(musician)
        #     musicians_dict.append(m)
        return Response(musicians.values())