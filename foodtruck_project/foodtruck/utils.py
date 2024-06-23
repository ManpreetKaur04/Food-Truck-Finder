
from geopy.distance import distance
from .models import FoodTruck

def get_nearest_food_trucks(user_lat, user_lon, n=5):
    food_trucks = FoodTruck.objects.all()
    food_trucks_with_distance = [
        (truck, distance((user_lat, user_lon), (truck.latitude, truck.longitude)).km)
        for truck in food_trucks
    ]
    food_trucks_with_distance.sort(key=lambda x: x[1])
    return [truck for truck, dist in food_trucks_with_distance[:n]]
