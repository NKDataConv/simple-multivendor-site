from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields.related import OneToOneField


class Neighbor(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    postal_code = models.IntegerField(default=0)
    street_name = models.CharField(max_length=255, default="")
    street_number = models.CharField(max_length=5, default=0)
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.OneToOneField(User, related_name='neighbor', on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
