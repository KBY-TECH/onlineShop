from django.contrib import admin
from .models import *


class OrderAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','created','updated','paid',
                    ]
    list_filter = ['created', 'updated', 'paid']
    search_fields = ['first_name','last_name']


admin.site.register(Order, OrderAdmin)