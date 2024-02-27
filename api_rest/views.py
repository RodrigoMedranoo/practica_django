from django.shortcuts import render
from rest_framework import viewsets
from .models import Comida, Bebida
from .serializer import ComidaSerializer, BebidaSerializer
# Create your views here.

class ComidaViewset(viewsets.ModelViewSet):
    queryset = Comida.objects.all()
    serializer_class = ComidaSerializer

class BebidaViewset(viewsets.ModelViewSet):
    queryset = Bebida.objects.all()
    serializer_class = BebidaSerializer
