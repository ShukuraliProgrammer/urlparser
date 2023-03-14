from django.contrib import admin
from django.contrib.auth.models import User, Group
from parser.models import UrlParser

admin.site.unregister(User)
admin.site.unregister(Group)


class UrlParserAdmin(admin.ModelAdmin):
    list_display = ['url', 'text', 'result', 'created_at', 'updated_at']


admin.site.register(UrlParser, UrlParserAdmin)

# Register your models here.
