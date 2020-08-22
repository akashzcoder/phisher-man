from phish_manager.phisherman.models import Incident, Email
from rest_framework import serializers

class IncidentSerializer(serializers.Serializer):
    # This describes how the data will be validated
    id = serializers.IntegerField(read_only=True)
    url = serializers.CharField(required=False, allow_blank=False)
    client = serializers.CharField(required=False, allow_blank=False)
    active = serializers.BooleanField(default=True)
    created = serializers.DateTimeField(read_only=True)

    # Create a new Incident instance given validated data
    def create(self, validated_data):
        return Incident.objects.create(**validated_data)

    # Update existing incident instance given validated data
    def update(self, instance, validated_data):
        instance.url = validated_data.get('url', instance.url)
        instance.client = validated_data.get('client', instance.client)
        instance.active = validated_data.get('active', instance.active)
        instance.save()
        return instance


class EmailSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.CharField(max_length=1024, allow_blank=True)
    created = serializers.DateTimeField(read_only=True)

    # Create a new Incident instance given validated data
    def create(self, validated_data):
        return Email.objects.create(**validated_data)
