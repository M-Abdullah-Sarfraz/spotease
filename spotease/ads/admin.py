from django.contrib import admin
from .models import Ad  # Import your Ad model

@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'location', 'price', 'created_at']
    search_fields = ['title', 'category', 'user__username']
