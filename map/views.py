import folium
from django.shortcuts import render
from django.conf import settings


def update_map(request, lat, lon):
    m = folium.Map([lat, lon], zoom_start=20)
    test = folium.Html('<b>Hallo Immanuel!</b>', script=True)
    popup = folium.Popup(test, max_width=2650)
    folium.RegularPolygonMarker(location=[47.9953, 7.8531], popup=popup).add_to(m)
    m=m._repr_html_() #updated
    context = {'my_map': m}

    return render(request, 'map/only_map.html', context)


def autocomplete(request):
    m = folium.Map([47.995, 7.853], zoom_start=10)
    test = folium.Html('<b>Hallo Immanuel!</b>', script=True)
    popup = folium.Popup(test, max_width=2650)
    folium.RegularPolygonMarker(location=[47.9953, 7.8531], popup=popup).add_to(m)
    m=m._repr_html_() #updated

    context = {'my_map': m,
               'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY}

    return render(request, 'map/map.html', context)
