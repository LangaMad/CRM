from django.contrib import admin
from .models import Apartment,Building
# Register your models here.



@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    list_display = ['id','number','price','building','floor','area','ready_date','status','client','effect_status','manager' ]
    list_filter = ['price','area','status']
    search_fields = ['number', 'price',]


@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    list_display = ['id','name']
    search_fields = ['name']




