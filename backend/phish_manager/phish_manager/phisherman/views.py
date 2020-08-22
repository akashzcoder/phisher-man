from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from phish_manager.phisherman.models import Incident
from phish_manager.phisherman.serializers import IncidentSerializer

@api_view(['GET', 'POST'])
def incident_list(request):
    # List the incidents or create a new incident
    if request.method == 'GET':
        incidents = Incident.objects.all()
        serializer = IncidentSerializer(incidents, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = IncidentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)