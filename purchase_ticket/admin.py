from django.contrib import admin
from .models import Purchase

# Register your models here.
@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ( 'purchase_date','quantity',)
    search_fields = ('ticket', 'user',)
    list_filter = ('purchase_date',)
