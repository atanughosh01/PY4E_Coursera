""" In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/json2.py.
The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract
the comment counts from the JSON data, compute the sum of the numbers in the file and enter the sum below:
SAMPLE DATA : http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553) """

import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Enter http://py4e-data.dr-chuck.net/comments_42.json as URL
url = input("\nEnter URL : ")
data = urllib.request.urlopen(url, context=ctx).read().decode()
print(f"\nRetrieving : {url}")
print(f"\nRetrieved {len(data)} characters")

info = json.loads(data)
# print(f"\nINFO : {info}")
# print("\nComments : ", info["comments"])

num_list = list()
for item in info["comments"]:
    num_list.append(int(item["count"]))

print("\nNumber List :", num_list)
print("\nTotal numbers present in the list :", len(num_list))
print("\nSum of Numbers :", sum(num_list), "\n")
