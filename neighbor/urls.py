from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name = 'neighbor'


urlpatterns = [
    path('become-neighbor/', views.become_neighbor, name="become-neighbor"),
    path('add-food/', views.add_food, name="add-food"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('login/', auth_views.LoginView.as_view(template_name='neighbor/login.html'), name="login"),
]
