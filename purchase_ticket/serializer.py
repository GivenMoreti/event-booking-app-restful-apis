from rest_framework import serializers
from .models import Purchase

class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields= "__all__"

        def validate_event_title(self, value):
            if Purchase.objects.filter(ticket__iexact=value).exists():
                raise serializers.ValidationError("The ticket already exists.")
            return value