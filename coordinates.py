import firebase_admin
from firebase_admin import db,credentials

cred = credentials.Certificate("Credentials-firebase.json")
thing = firebase_admin.initialize_app(cred, {"databaseURL": "https://refill-radar-database-default-rtdb.firebaseio.com/.json" })
print(thing.credential)
ref = db.reference("/")
location = db.reference("/Locations").get()
library = location.get("Library")
print(library)