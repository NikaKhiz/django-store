from django.contrib import admin
from .models import Usercart

@admin.register(Usercart)
class UserCartAdmin(admin.ModelAdmin):
    list_display = ('user',)  
    search_fields = ('user__username',) 
    list_filter = ('user',)  
