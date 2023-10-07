#import haversine as hs
#from haversine import Unit
#
#loc1=(19.0760, 72.8777)
#loc2=(18.5204, 73.8567)
#
#result=hs.haversine(loc1, loc2, unit=Unit.MILES)
#print("The distance calculated is: %.2f miles." % result)

from math import cos, asin, sqrt

def distance(lat1, lon1, lat2, lon2):
    p = 0.017453292519943295
    hav = 0.5 - cos((lat2-lat1)*p)/2 + cos(lat1*p)*cos(lat2*p) * (1-cos((lon2-lon1)*p)) / 2
    return 12742 * asin(sqrt(hav))

def closest(data, v):
    return min(data, key=lambda p: distance(v['lat'],v['lon'],p['lat'],p['lon']))

tempDataList = [{'lat': 28.59573, 'lon': -81.19955}, 
                {'lat': 28.60188,  'lon': -81.20035}, 
                {'lat': 28.59369, 'lon': -81.19879},
                {'lat': 28.60057, 'lon': -81.20060},
                {'lat': 28.600282664646766, 'lon': -81.20133586270218}]
v = {'lat': 28.606139, 'lon': -81.1969788}
print(closest(tempDataList, v))