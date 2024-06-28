from django.db import models
from django.contrib.auth.models import User
from ticket.models import Ticket

# Create your models here.
class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='purchases')
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name='purchases')
    quantity = models.PositiveIntegerField(verbose_name="Quantity Purchased")
    purchase_date = models.DateTimeField(auto_now_add=True, verbose_name="Purchase Date")

    def __str__(self):
        return f"Purchase by {self.user.username} for {self.ticket.event.event_title}"

    def total_cost(self):
        return self.ticket.price * self.quantity