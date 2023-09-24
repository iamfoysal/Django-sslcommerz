from django.contrib import admin
from .models import *

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('name', 'card_no', 'amount',  'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('currency', 'status')



admin.site.register(Transaction, TransactionAdmin)
admin.site.register(PaymentGateway)
