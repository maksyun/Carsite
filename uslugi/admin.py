# -*- coding: utf8 -*-

from django.contrib import admin
from models import Uslugi

class UslugiAdmin(admin.ModelAdmin):
    list_display = ('title', 'status')
    list_filter = ('title',)
    serch_fields = ('title')
    
    
admin.site.register(Uslugi, UslugiAdmin)
