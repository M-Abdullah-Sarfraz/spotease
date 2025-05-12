from django.contrib import admin
from .models import AdPayment

@admin.register(AdPayment)
class AdPaymentAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'location', 'price', 'account_holder_name', 'account_number', 'bank', 'created_at']
    search_fields = ['title', 'category', 'account_holder_name']
