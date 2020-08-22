from phish_manager.phisherman.models import Incident
from rest_framework import serializers

class IncidentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    url = serializers.CharField(required=True, allow_blank=False)
    client = serializers.CharField(required=True, allow_blank=False)
    active = serializers.BooleanField(default=True)
    created = serializers.DateTimeField(read_only=True)

    # Create a new Incident instance given validated data
    def create(self, validated_data):
        return Incident.objects.create(**validated_data)

    # Update existing incident instance given validated data
    def update(self, instance, validated_data):
        instance.url = validated_data.get('url', instance.url)
        instance.active = validated_data.get('active', instance.active)
        instance.save()
        return instance