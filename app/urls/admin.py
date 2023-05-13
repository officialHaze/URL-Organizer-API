from django.contrib import admin
from .models import URL, SingleLink

class URLView(admin.ModelAdmin):
    model = URL
    list_display = ('id', 'pid', 'long_url', 'short_url', 'created')


class SingleLinkView(admin.ModelAdmin):
    model = SingleLink
    list_display = ('id', 'short_id', 'single_link', 'short_url', 'created')


admin.site.register(URL, URLView)
admin.site.register(SingleLink, SingleLinkView)
