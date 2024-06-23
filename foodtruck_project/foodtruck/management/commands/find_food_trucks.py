from django.core.management.base import BaseCommand
from foodtruck.models import FoodTruck
from django.db.models.functions import ACos, Cos, Radians, Sin
from django.db.models import F

class Command(BaseCommand):
    help = 'Find nearby food trucks'

    def add_arguments(self, parser):
        parser.add_argument('latitude', type=float, help='Latitude of the location')
        parser.add_argument('longitude', type=float, help='Longitude of the location')

    def handle(self, *args, **options):
        lat = options['latitude']
        lon = options['longitude']

        trucks = FoodTruck.objects.annotate(
            distance=ACos(
                Sin(Radians(lat)) * Sin(Radians(F('latitude'))) +
                Cos(Radians(lat)) * Cos(Radians(F('latitude'))) * Cos(Radians(F('longitude')) - Radians(lon))
            ) * 6371  # Radius of Earth in km
        ).order_by('distance')[:5]

        for truck in trucks:
            self.stdout.write(f"{truck.name} - {truck.address} - {truck.distance:.2f} km away")
