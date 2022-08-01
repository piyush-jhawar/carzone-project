from django.contrib import admin
from django.utils.html import format_html

from pages.models import Team, CompanyDetail

# Register your models here.


class TeamAdmin(admin.ModelAdmin):

    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius:50px;" />'.format(object.photo.url))

    thumbnail.short_description = "Photo"

    list_display = ('id', 'thumbnail', 'first_name',
                    'designation', 'created_date', 'modified_date')
    list_display_links = ('id', 'thumbnail', 'first_name',)
    search_fields = ('id', 'first_name', 'last_name', 'designation')
    list_filter = ('designation',)


class CompanyDetailAdmin(admin.ModelAdmin):

    list_display = ('title', 'mobile', 'fax', 'email',
                    'startday', 'endday', 'opentime', 'closetime')
    list_display_links = ('title',)
    # search_fields = ('id', 'first_name', 'last_name', 'designation')
    # list_filter = ('designation',)


admin.site.register(Team, TeamAdmin)
admin.site.register(CompanyDetail, CompanyDetailAdmin)
