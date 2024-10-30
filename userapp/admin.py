from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_active_datetime', 'is_active', 'is_staff', 'date_joined',)
    search_fields = ('username','email')
    ordering = ('username',)
    list_editable = ('email', 'first_name', 'is_active', 'is_active', 'is_staff')