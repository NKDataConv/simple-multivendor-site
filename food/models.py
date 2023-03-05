from django.db import models
from neighbor.models import Neighbor


class Food(models.Model):
    neighbor = models.ForeignKey(Neighbor, related_name="food", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
