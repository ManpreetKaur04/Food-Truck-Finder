import csv
from django.core.management.base import BaseCommand
from foodtruck.models import FoodTruck

class Command(BaseCommand):
    help = 'Load food trucks from a CSV file'

    def handle(self, *args, **kwargs):
        with open('/Users/kamaljeetsingh/Desktop/myproject/foodtruck_project/food-truck-data.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                FoodTruck.objects.create(
                    name=row['Applicant'],
                    latitude=row['Latitude'],
                    longitude=row['Longitude'],
                    address=row['Address']
                )
        self.stdout.write(self.style.SUCCESS('Successfully loaded food trucks'))
