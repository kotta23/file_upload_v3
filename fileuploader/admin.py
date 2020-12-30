from django.contrib import admin
from .models import DesignFile

# Register your models here.

class ListingAdmin(admin.ModelAdmin):
    list_display = (  'file', 'done','list_date') #display dollar amount rather than price
    search_fields = ( 'file', 'done','list_date')
    list_per_page = 25
admin.site.register(DesignFile,ListingAdmin)


