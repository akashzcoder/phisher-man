from django.db import models

# Create your models here.

class Incident(models.Model):
    client = models.CharField(max_length=100, blank=False, default='Undefined')
    url = models.URLField()
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']