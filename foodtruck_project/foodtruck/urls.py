from django.urls import path
from . import views
from .views import NearbyFoodTrucks, index, get_nearest_food_trucks_view

urlpatterns = [
    path('', index, name='index'),
    path('api/foodtrucks/nearby/<str:latitude>/<str:longitude>/', NearbyFoodTrucks.as_view(), name='nearby-foodtrucks'),
    path('api/foodtrucks/nearby/<str:lat>/<str:lon>/', views.get_nearest_food_trucks_view, name='get_nearest_food_trucks'),
]
