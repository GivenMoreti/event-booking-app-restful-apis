from rest_framework import serializers
from .models import Venue

class VenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venue
        fields= "__all__"

    def validate_venue_name(self, value):
            if Venue.objects.filter(venue_name__iexact=value).exists():
                raise serializers.ValidationError("The vanue name already exists.")
            return value
