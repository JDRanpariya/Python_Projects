from django.shortcuts import render
from .models import Performer
from .serializers import PerformerSerializer 
from rest_framework import generics
# Create your views here.


class PerformerView(generics.ListCreateAPIView):
    queryset = Performer.objects.all()
    serializer_class = PerformerSerializer