from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import FoodTruck
from .serializers import FoodTruckSerializer
from django.db.models.functions import ACos, Cos, Radians, Sin
from django.db.models import F, Value
from django.shortcuts import render
from django.http import JsonResponse
from .utils import get_nearest_food_trucks


def index(request):
    return render(request, 'foodtruck/index.html')

class NearbyFoodTrucks(APIView):
    def get(self, request, latitude, longitude):
        try:
            lat = float(latitude)
            lon = float(longitude)
        except ValueError:
            return Response({"error": "Invalid coordinates"}, status=status.HTTP_400_BAD_REQUEST)

        trucks = FoodTruck.objects.annotate(
            distance=ACos(
                Sin(Radians(lat)) * Sin(Radians(F('latitude'))) +
                Cos(Radians(lat)) * Cos(Radians(F('latitude'))) * Cos(Radians(F('longitude')) - Radians(lon))
            ) * 6371  # Radius of Earth in km
        ).order_by('distance')[:5]

        serializer = FoodTruckSerializer(trucks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
def get_nearest_food_trucks_view(request, lat, lon):
    user_lat = float(lat)
    user_lon = float(lon)
    nearest_food_trucks = get_nearest_food_trucks(user_lat, user_lon)
    
    data = [
        {'name': truck.name, 'latitude': truck.latitude, 'longitude': truck.longitude}
        for truck in nearest_food_trucks
    ]
    return JsonResponse(data, safe=False)
