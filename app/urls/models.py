from django.db import models
from django.utils.translation import gettext_lazy as _

class URL(models.Model):
    long_url = models.TextField(_("Long Url"))
    short_url = models.CharField(_("Short Url"), max_length=200)
    created = models.DateTimeField(_("Created on"), auto_now_add=True)

    def __str__(self):
        return self.short_url
