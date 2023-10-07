import firebase_admin
from firebase_admin import db,credentials

cred = credentials.Certificate("Credentials-firebase.json")
thing = firebase_admin.initialize_app(cred, {"databaseURL": "https://refill-radar-database-default-rtdb.firebaseio.com/.json" })
ref = db.reference("/")
location = db.reference("/Locations").get()
neptune_long = (location.get("Neptune").get("Long:"))
rwc_long = (location.get("RWC").get("Long:"))
library_long = (location.get("Library").get("Long:"))
student_union_long = (location.get("Student Union").get("Long:"))
tech_commons_long = (location.get("Tech Commons 2").get("Long:"))


neptune_lat = (location.get("Neptune").get("Lat:"))
rwc_lat = (location.get("RWC").get("Lat:"))
library_lat = (location.get("Library").get("Lat:"))
student_union_lat = (location.get("Student Union").get("Lat:"))
tech_commons_lat = (location.get("Tech Commons 2").get("Lat:"))


long_list = [neptune_long,rwc_long,library_long,student_union_long,tech_commons_long]
lat_list = [neptune_lat,rwc_lat,library_lat,student_union_lat,tech_commons_lat]
print(long_list)
print(lat_list)

