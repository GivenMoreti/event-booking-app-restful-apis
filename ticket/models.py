from django.db import models
from event_app.models import Event
from venue.models import Venue

# Create your models here.
TICKET_TYPES = (
        ('standard', 'Standard'),
        ('vip', 'VIP'),
        ('student', 'Student'),
    )



class Ticket(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='tickets')
    ticket_type = models.CharField(max_length=50,choices=TICKET_TYPES, verbose_name="Ticket Type")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Price")
    quantity = models.PositiveIntegerField(verbose_name="Quantity")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    def __str__(self):
        return f"{self.ticket_type} for {self.event.event_title}"
    
    class Meta:
        ordering = ["-updated_at"]          #show latest first


    def calculate_total_ticket_cost(self):
        return self.price * self.quantity
    
    def get_number_tickets(self):
      
        return Venue.venue_size         #venue size determines the number of tickets that can be purchased
    