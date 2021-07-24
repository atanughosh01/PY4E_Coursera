""" In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geoxml.py.
The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the
comment counts from the XML data, compute the sum of the numbers in the file.
SAMPLE DATA : http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553) """

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Enter http://py4e-data.dr-chuck.net/comments_42.xml as the test url
url = input("\nEnter URL : ")
data = urllib.request.urlopen(url, context=ctx).read()
print("\nRetrieving :", url)
print("\nRetrieved :", len(data), "characters")

tree = ET.fromstring(data)
lst = tree.findall("comments/comment")
# To make the code a little simpler, we can use an XPath selector string to look through
# the entire tree of XML for any tag named 'count' with the following line of code:
# counts = tree.findall('.//count')

print("\nNumbers are :", end=" ")
num_list = list()

for item in lst:
    num = item.find("count").text
    num_list.append(int(num))
    print(num, end=" ")

print("\n\nCount of numbers in the URL =", len(num_list))
print("\nSum of Numbers =", sum(num_list), "\n")
