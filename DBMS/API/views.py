from django.shortcuts import render
from rest_framework import viewsets
from .serializers import SongSerializer
from .models import Songs


class SongViewSet(viewsets.ModelViewSet):
    queryset = Songs.objects.all().order_by('name')
    serializer_class = SongSerializer