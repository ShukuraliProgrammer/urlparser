from django.contrib import admin
from django.contrib.auth.models import User, Group
from urlpapp.models import UrlParser




class UrlParserAdmin(admin.ModelAdmin):
    list_display = ['url', 'text', 'result', 'created_at', 'updated_at']


admin.site.register(UrlParser, UrlParserAdmin)

# Register your models here.
