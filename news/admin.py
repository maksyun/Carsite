# -*- coding: utf8 -*-

from django.contrib import admin
from models import CarNews

class CarNewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created')
    list_filter = ('created',)
    serch_fields = ('title', 'created', 'content')
    
    
admin.site.register(CarNews, CarNewsAdmin)
