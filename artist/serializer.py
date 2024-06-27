from rest_framework import serializers
from .models import Artist

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields= "__all__"

        def validate_artist_name(self, value):
            if Artist.objects.filter(artist_name__iexact=value).exists():
                raise serializers.ValidationError("The artist name already exists.")
            return value