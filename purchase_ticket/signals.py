from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Purchase

@receiver(post_save, sender=Purchase)
def update_venue_size(sender, instance, created, **kwargs):
    if created:
        instance.decrement_tickets_on_purchase()