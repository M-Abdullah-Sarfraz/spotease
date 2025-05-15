from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    
    list_display = ('get_full_name', 'email', 'username', 'is_staff', 'is_active')
    
    search_fields = ('first_name', 'last_name', 'email', 'username')

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"
    get_full_name.short_description = 'Full Name'  
admin.site.register(CustomUser, CustomUserAdmin)
