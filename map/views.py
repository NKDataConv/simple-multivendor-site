import folium
from django.shortcuts import render
from django.conf import settings
from food.models import Food
from pydantic import BaseModel


class MapMarker(BaseModel):
    food_id: int
    title: str
    price: str
    latitude: float
    longitude: float


def get_all_foods():
    foods = Food.objects.all()

    map_marker = []
    for food in foods:
        map_marker.append(MapMarker(food_id=food.id, title=food.title, price=food.price, latitude=food.neighbor.latitude, longitude=food.neighbor.longitude))
    return map_marker


def update_map(request, lat, lon):
    m = folium.Map([lat, lon], zoom_start=20)

    map_marker = get_all_foods()
    for marker in map_marker:
        html_for_popup = folium.Html(f'<b>{marker.title}</b><br>Price: {marker.price}<br><a href="/food_order/{marker.food_id}">Bestellen</a>', script=True)
        popup = folium.Popup(html_for_popup, max_width=2650)
        folium.RegularPolygonMarker(location=[marker.latitude, marker.longitude], popup=popup).add_to(m)

    m=m._repr_html_() #updated
    context = {'my_map': m}

    return render(request, 'map/only_map.html', context)


def autocomplete(request):
    m = folium.Map([47.995, 7.853], zoom_start=10)
    m=m._repr_html_() #updated
    context = {'my_map': m,
               'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY}

    return render(request, 'map/map.html', context)
