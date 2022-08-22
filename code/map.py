import googlemaps


""" uses google API to access gooogle maps.
this function calculates the distance between two locations and returns the distance in miles as an integer value
*start = starting address of journey
*destination = addresss of final destination"""

def calculate_distance(start, destination):
    
   API_KEY = ''
   map_client = googlemaps.Client(API_KEY)
   
    
   distance = map_client.distance_matrix(start, destination)
   try:
       distance_meters = distance.get('rows')[0].get('elements')[0].get('distance').get('value')
   except AttributeError:
       distance_meters = 0

   distance_in_miles = distance_meters / 1608
   
   return distance_in_miles

