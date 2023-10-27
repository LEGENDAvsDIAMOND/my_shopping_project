from django.shortcuts import render
from rest_framework import generics
from .models import MainCus
from .serializers import MainCusSerializer

class MainCusListCreateView(generics.ListCreateAPIView):
    queryset = MainCus.objects.all()
    serializer_class = MainCusSerializer

class MainCusRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MainCus.objects.all()
    serializer_class = MainCusSerializer
