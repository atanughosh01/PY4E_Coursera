""" for testing json parsing using json package """

import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False

if api_key is False:
    api_key = 42
    service_url = "http://py4e-data.dr-chuck.net/json?"
else:
    service_url = "https://maps.googleapis.com/maps/api/geocode/json?"

# ignore ssl certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input("Enter Location : ")
    if len(address) < 1:
        break

    parms = dict()
    parms["address"] = address
    if api_key is not False:
        parms["key"] = api_key
    url = service_url + urllib.parse.urlencode(parms)

    print("Retrieving :", url)
    data = urllib.request.urlopen(url, context=ctx).read().decode()
    print(f"Retrieved : {len(data)} characters")

    try:
        js = json.loads(data)
    except Exception as e:
        js = None

    if not js or "status" not in js or js["status"] != "ok":
        print("==== Failure To Retrieve ====")
        print(data)
        continue

print(json.dumps(js, indent=4))

lat = js["result"][0]["geometry"]["location"]["lat"]
lng = js["result"][0]["geometry"]["location"]["lng"]
print(f"lat {lat} lng {lng}")
location = js["results"][0]["formatted_address"]
print(location)
