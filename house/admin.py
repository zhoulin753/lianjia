from django.contrib import admin
from .models import House
# Register your models here.
# @admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'houseinfo', 'area', 'finish', 'house_type',
                    'floor', 'address', 'cost', 'price', 'url']
    list_per_page = 30

    search_fields = ('price',)
admin.site.register(House,HouseAdmin)