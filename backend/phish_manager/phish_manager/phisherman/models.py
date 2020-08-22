from django.db import models

class Incident(models.Model):
    url = models.URLField()
    client = models.CharField(max_length=100, blank=False, default='Undefined')
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']


class Email(models.Model):
    email = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']
