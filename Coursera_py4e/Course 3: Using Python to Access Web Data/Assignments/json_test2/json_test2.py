""" For testing json parsing using json package. """

import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    print("\n---------------------------------------------")
    # Enter "Ann Arbor, MI" as the test location
    address = input("\nEnter location: ")
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print("Parms :", parms)
    print("Last portion of URL :", urllib.parse.urlencode(parms))
    print("Retrieving :", url)

    data = urllib.request.urlopen(url, context=ctx).read().decode()
    print("Retrieved :", len(data), "characters")

    try:
        js = json.loads(data)
    except Exception as e:
        js = None
        print("JSON Load Error :", e)

    if not js or "status" not in js or js["status"] != "OK":
        print("==== Failed To Retrieve ====")
        print("Data :", data)
        continue

    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']
    location = js['results'][0]['formatted_address']

    print("JSON :", json.dumps(js, indent=4))
    print("Latitude :", lat, "\nLongitude :", lng)
    print("Location :", location)
