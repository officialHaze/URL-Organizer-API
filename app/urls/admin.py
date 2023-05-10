from django.contrib import admin
from .models import URL

class URLView(admin.ModelAdmin):
    model = URL
    list_display = ('id', 'long_url', 'short_url', 'created')


admin.site.register(URL, URLView)
