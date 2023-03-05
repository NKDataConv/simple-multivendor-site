from django.forms import ModelForm, models
from django.contrib.auth.forms import UserCreationForm

from food.models import Food
from .models import Neighbor
from django import forms
from geopy.geocoders import Nominatim


class FoodForm(ModelForm):
    class Meta:
        model = Food
        fields = ['title', 'price']

class NeighborCreationForm(UserCreationForm):
    city = forms.CharField(max_length=255)
    postal_code = forms.IntegerField()
    street_name = forms.CharField(max_length=255)
    street_number = forms.CharField(max_length=5)

    def get_coordinates(self):
        geolocator = Nominatim(user_agent="neighbor")
        location = geolocator.geocode(f"{self.cleaned_data['street_name']} {self.cleaned_data['street_number']}, {self.cleaned_data['postal_code']} {self.cleaned_data['city']}")
        return location.latitude, location.longitude

    def save(self, commit=True):
        user = super().save(commit=False)
        user.save()
        neighbor = Neighbor.objects.create(
            name=user.username,
            city=self.cleaned_data['city'],
            postal_code=self.cleaned_data['postal_code'],
            street_name=self.cleaned_data['street_name'],
            street_number=self.cleaned_data['street_number'],
            latitude = self.get_coordinates()[0],
            longitude = self.get_coordinates()[1],
            created_by=user
        )
        return user
