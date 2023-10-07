from firebase_admin import db

ref = db.reference('https://refill-radar-database-default-rtdb.firebaseio.com/')

class Retrieve:
    def _init_(self, location, longitude, latitude, image, direction):
        self.location = location
        self.longitude = longitude
        self.latitude = latitude
        self.image = image
        self.direction = direction

    def _repr_(self):
        return f"Location(\
                location={self.location}, \
                longitude={self.longitude}, \
                latitude={self.latitude}, \
                image={self.image}, \
                direction={self.direction}\
            )"
