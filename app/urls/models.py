from django.db import models
from django.utils.translation import gettext_lazy as _

class URL(models.Model):
    pid = models.CharField(_("PID"), max_length=20)
    long_url = models.TextField(_("Long Url"))
    short_url = models.CharField(_("Short Url"), max_length=200)
    created = models.DateTimeField(_("Created on"), auto_now_add=True)

    def __str__(self):
        return self.short_url


'''Single link model'''
class SingleLink(models.Model):
    short_id = models.CharField(_("SID"), max_length=20)
    single_link = models.CharField(_("Single Link"), max_length=200)
    short_url = models.ForeignKey(to=URL, on_delete=models.CASCADE)
    created = models.DateTimeField(_("Created on"), auto_now_add=True)

    def __str__(self):
        return self.single_link
