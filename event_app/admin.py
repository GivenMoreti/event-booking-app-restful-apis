from django.contrib import admin
from .models import Event

# Register your models here.
class EventModel(admin.ModelAdmin):
    list_display =("event_title","event_location","event_start_date","event_created","event_modified")
    search_fields = ('event_title', 'event_location')
    list_filter = ('event_start_date', 'event_created')
    
admin.site.register(Event,EventModel)