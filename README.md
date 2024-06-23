# Food-Truck-Finder
Finds you the closet food trucks near you in San Francisco .

Taste Trails is a web application that helps users find nearby food trucks based on their current location. The application uses the Leaflet library for map rendering and JQuery for handling API requests.

Features
* Interactive Map: Displays an interactive map using Leaflet.
* Location Input: Allows users to enter latitude and longitude to find food trucks near a specific location.
* Nearby Food Trucks: Displays a list of nearby food trucks and their locations on the map.
* Responsive Design: Uses Bootstrap for a responsive and user-friendly interface.

Usage

1. Web API that returns a set of food trucks in JSON format.[GET /api/foodtrucks/nearby/:latitude/:longitude/]
(Use the API endpoint directly (e.g., http://127.0.0.1:8000/api/foodtrucks/nearby/<latitude>/<longitude>/) to get JSON responses for nearby food trucks.)
The API returns a JSON array of food trucks, each with the following properties:
* name: The name of the food truck.
* address: The address of the food truck.
* latitude: The latitude of the food truck.
* longitude: The longitude of the food truck.

2. Web frontend that visualizes the nearby food trucks
(python3 manage.py runserver)
-Open the application in your web browser.
-Enter the latitude and longitude of your location.
-Click on the "Search" button.
-View the map to see your location and nearby food trucks.
-Check the list of food trucks displayed below the map.

3. CLI that gives us a couple of local options
Run the custom command to test: cli python manage.py find_food_trucks <latitude> <longitude>


Technologies Used
* Leaflet: For interactive maps.
* JQuery: For handling form submissions and API requests.
* Bootstrap: For styling and responsive design.
* OpenStreetMap: For map tiles.
* Django REST framework


