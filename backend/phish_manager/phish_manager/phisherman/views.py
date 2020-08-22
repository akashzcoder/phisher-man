from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from phish_manager.phisherman.models import Incident
from phish_manager.phisherman.serializers import IncidentSerializer

# Create your views here.

class IncidentViewSet(viewsets.ModelViewSet):
    # Incidents will be viewed and edited here
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer
    permission_classes = [permissions.IsAuthenticated]