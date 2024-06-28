from django.contrib import admin
from .models import Venue

# Register your models here.
@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('venue_name', 'venue_size','venue_location', 'created_at', 'modified_at')
    search_fields = ('venue_name', 'venue_location')
    list_filter = ('venue_name', 'created_at')
