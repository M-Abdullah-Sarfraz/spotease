from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    # Display full name and email in the list view
    list_display = ('get_full_name', 'email', 'username', 'is_staff', 'is_active')
    # Enable searching by full name and email
    search_fields = ('first_name', 'last_name', 'email', 'username')

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"
    get_full_name.short_description = 'Full Name'  # Column name in the admin

# Register the CustomUser model with the customized admin
admin.site.register(CustomUser, CustomUserAdmin)
