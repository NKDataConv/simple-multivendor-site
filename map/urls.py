from . import views
from . import converters
from django.urls import path, register_converter


register_converter(converters.FloatUrlParameterConverter, 'float')

urlpatterns = [
    path('', views.autocomplete, name="map"),
    path('update_map/<float:lat>/<float:lon>/', views.update_map, name="update_map"),
]
