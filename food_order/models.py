from django.db import models
from food.models import Food
from neighbor.models import Neighbor


class FoodOrder(models.Model):
    food = models.ForeignKey(Food, related_name="food", on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered_by = models.ForeignKey(Neighbor, related_name="cook", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
