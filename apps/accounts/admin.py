from django.contrib import admin
from .models import Manager
# Register your models here.



@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    list_display = ['full_name','phone_number','email','number_of_deals']
    search_fields = ['full_name','phone_number','email']
    list_filter = ['full_name','phone_number','email','created_at']
    list_per_page = 10
    ordering = ['full_name','created_at']


