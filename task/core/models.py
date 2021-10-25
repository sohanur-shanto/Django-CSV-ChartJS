from django.db import models
from django.utils.translation import activate


class Csv(models.Model):
    file_name = models.FileField(upload_to='core')
    uploaded = models.DateTimeField(auto_now_add=True)
    activated = models.BooleanField(default=False)


class Data(models.Model):
    date = models.CharField(max_length=200)
    appl_open = models.DecimalField(max_digits=100, decimal_places=10, blank=True, null=True)
    appl_high = models.DecimalField(max_digits=100, decimal_places=10, blank=True, null=True)
    appl_low = models.DecimalField(max_digits=100, decimal_places=10, blank=True, null=True)
    appl_close = models.DecimalField(max_digits=100, decimal_places=10, blank=True, null=True)
    appl_volume = models.DecimalField(max_digits=100, decimal_places=10, blank=True, null=True)
    appl_adjusted = models.DecimalField(max_digits=100, decimal_places=10, blank=True, null=True)
    dn = models.DecimalField(max_digits=100, decimal_places=10, blank=True, null=True)
    mavg = models.DecimalField(max_digits=100, decimal_places=10, blank=True, null=True)
    up = models.DecimalField(max_digits=100, decimal_places=10, blank=True, null=True)
    direction = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    