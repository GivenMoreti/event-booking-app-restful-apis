from rest_framework import serializers
from .models import Event

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields= "__all__"

        def validate_event_title(self, value):
            if Event.objects.filter(event_title__iexact=value).exists():
                raise serializers.ValidationError("The event already exists.")
            return value