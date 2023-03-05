from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name = 'food_order'


urlpatterns = [
    path('<int:food_id>/', views.order_food, name="food-order")
]
