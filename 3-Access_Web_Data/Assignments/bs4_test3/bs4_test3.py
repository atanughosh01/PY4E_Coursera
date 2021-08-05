""" In this assignment you will write a Python program that expands on http://www.py4e.com/code3/urllinks.py.
The program will use urllib to read the HTML from the data files below, extract the href= values from the
anchor tags, scan for a tag that is in a particular position relative to the first name in the list, follow
that link and repeat the process a number of times and report the last name you find.
SAMPLE DATA : http://py4e-data.dr-chuck.net/known_by_Fikret.html """

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter URL : ")
repetition_count = int(input("Enter Count : "))
pos = int(input("Enter Position : ")) - 1

for i in range(repetition_count):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup("a")
    # print(tags)
    link = tags[pos].get("href", None)
    # print(link)
    url = link
    print("\nRetrieving :", link)
    name = tags[pos].contents[0]
    print("Name Found :", name)
