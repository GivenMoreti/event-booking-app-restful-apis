from django.contrib import admin
from .models import Ticket


# Register your models here.
@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('event', 'ticket_type', 'price', 'quantity', 'created_at', 'updated_at')
    search_fields = ('event__event_title', 'ticket_type')
    list_filter = ('event', 'created_at')