"""
CALLING A JSON API
In this assignment, you will write a Python program somewhat similar to
http://www.py4e.com/code3/geojson.py. The program will prompt for a location,
contact a web service and retrieve JSON for the web service and parse that data,
and retrieve the first place_id from the JSON. A place ID is a textual identifier
that uniquely identifies a place within Google Maps.


API ENDPOINTS
To complete this assignment, you should use this API endpoint that has a static
a subset of the Google Data:

http://py4e-data.dr-chuck.net/json?

This API uses the same parameters (address) as the Google API. This
API also has no rate limit so you can test as often as you like.
If you visit the URL with no parameters, you get a "No address..." response.

To call the API, you need to include a key= parameter and the address
that you are requesting as the address= parameter that is properly URL encoded
using the urllib.parse.urlencode() fuction as shown in
http://www.py4e.com/code3/geojson.py

Make sure to check that your code is using the API endpoint is as shown above.
You will get different results from the geojson and json endpoints so make sure
you are using the same endpoint as this autograder is using.


TEST DATA / SAMPLE EXECUTION
You can test to see if your program is working with a location of "South Federal
University" which will have a place_id of "ChIJLzabHQ7i2IgRzeZb_AgUj0Q".


TURN IN
Please run your program to find the place_id for this location: Portland State University

Make sure to enter the name and case exactly as above and enter the place_id and
your Python code below. Hint: The first seven characters of the place_id are "ChIJkbA ...".

Make sure to retrieve the data from the URL specified above and
not the normal Google API. Your program should work with the Google API - but the
place_id may not match for this assignment.
"""

# import necessary packages
import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    service_url = "http://py4e-data.dr-chuck.net/json?"
else:
    service_url = "https://maps.googleapis.com/maps/api/geocode/json?"

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    # Enter "South Federal University" as address which has place_id of "ChIJLzabHQ7i2IgRzeZb_AgUj0Q"
    address = input("\nEnter Location (Type S and press ENTER to stop) : ")
    if len(address) < 1: break
    if address == "s" or address == "S":
        print("Process is being stopped....Process Stopped")
        quit()

    address_key_pair = dict()
    address_key_pair["address"] = address                           # add "address" key with value as address
    if api_key is not False:
        address_key_pair["key"] = api_key                           # add "key" key with value as api_key
    url = service_url + urllib.parse.urlencode(address_key_pair)    # generates the full url

    print("\nAddress and Key :", address_key_pair)
    print("Last portion of URL :", urllib.parse.urlencode(address_key_pair))
    print("\nRetrieving :", url)

    # open the URL, fetch, read and decode the contents of the generated URL
    data = urllib.request.urlopen(url, context=ctx).read().decode()
    print(f"Retrieved {len(data)} characters")

    try:
        info = json.loads(data)     # deserialize the json data into python data
    except Exception as e:
        info = None
        print(e)

    print("\nDATA :", data)
    print("INFO :", info)

    if not info or "status" not in info or info["status"] != "OK":  # if retrieved the wrong data/url
        print("==== Failed To Retrieve ====")                       # print error message
        print("Data :", data)
        continue

    place_id = info["results"][0]["place_id"]
    print(f"\nThe Place ID of {address} is : {place_id}")
