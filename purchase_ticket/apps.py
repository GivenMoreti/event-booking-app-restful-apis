from django.apps import AppConfig


class PurchaseTicketConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'purchase_ticket'

    def ready(self):
        import purchase_ticket.signals
