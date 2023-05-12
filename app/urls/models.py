from django.db import models
from django.utils.translation import gettext_lazy as _

class URL(models.Model):
    pid = models.CharField(_("PID"), max_length=20, null=True, default=None)
    long_url = models.TextField(_("Long Url"))
    short_url = models.CharField(_("Short Url"), max_length=200)
    created = models.DateTimeField(_("Created on"), auto_now_add=True)

    def __str__(self):
        return self.short_url
