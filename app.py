from flask import Flask, request, jsonify

app = Flask(__name__)

# A list of locations with their latitude and longitude
locations = [
    {"name": "Location A", "latitude": 28.59573, "longitude": -81.19955},
    {"name": "Location B", "latitude": 28.60188, "longitude": -81.20035},
    # Add more locations as needed
]

def calculate_distance(lat1, lon1, lat2, lon2):
    # Use the Haversine formula to calculate distance between two points
    import math
    radius = 6371  # Radius of the Earth in kilometers
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat/2)**2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    distance = radius * c
    return distance

@app.route('/')
def home():
    return open('index.html').read()

@app.route('/find_nearby')
def find_nearby():
    user_latitude = float(request.args.get('latitude'))
    user_longitude = float(request.args.get('longitude'))
    max_distance = float(request.args.get('max_distance'))

    nearby_locations = []

    for location in locations:
        dist = calculate_distance(user_latitude, user_longitude, location['latitude'], location['longitude'])
        if dist <= max_distance:
            nearby_locations.append(location['name'])

    return jsonify({'locations': nearby_locations})

if __name__ == '__main__':
    app.run(debug=True)
