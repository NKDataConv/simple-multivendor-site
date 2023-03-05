from django.forms import ModelForm, models
from django.contrib.auth.forms import UserCreationForm

from food.models import Food
from .models import FoodOrder
from django import forms
from geopy.geocoders import Nominatim


class FoodOrderForm(ModelForm):
    class Meta:
        model = FoodOrder
        fields = ['quantity']
