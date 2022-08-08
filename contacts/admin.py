from django.contrib import admin

# Register your models here.
from contacts.models import Contact
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'car_title', 'city', 'created_date', 'is_contacted', 'notes')
    list_display_links = ('id', 'first_name', 'last_name')
    search_fields = ('first_name', 'last_name', 'email', 'car_title')
    readonly_fields = ('user_id',)
    list_filter = ('is_contacted',)
    list_per_page = 25



admin.site.register(Contact, ContactAdmin)