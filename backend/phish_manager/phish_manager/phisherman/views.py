from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from phish_manager.phisherman.models import Incident
from phish_manager.phisherman.serializers import IncidentSerializer, EmailSerializer

@api_view(['GET', 'POST'])
def incident_list(request):
    # List the list of all incidents
    if request.method == 'GET':
        incidents = Incident.objects.all()
        serializer = IncidentSerializer(incidents, many=True)
        return Response(serializer.data)

    # Create a new incident
    elif request.method == 'POST':
        serializer = IncidentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def incident_details(request, id):
    # Fetch the incident with given ID
    try:
        incident = Incident.objects.get(id=id)
    except Incident.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # Return the serialized incident data
    if request.method == 'GET':
        serializer = IncidentSerializer(incident)
        return Response(serializer.data)

    # Update an incident and 
    # return either the data that was sent, or a 400 status response if something went wrong
    elif request.method == 'PUT':
        serializer = IncidentSerializer(incident, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Delete the incident and return a 204 status response
    elif request.method == 'DELETE':
        incident.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def post_email(request):
    if request.method == 'POST':
        serializer = EmailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
