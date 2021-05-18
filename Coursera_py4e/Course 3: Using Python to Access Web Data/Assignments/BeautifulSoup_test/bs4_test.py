""" for testing the bs4 library """

import urllib.request, urllib.request, urllib.error
from bs4 import BeautifulSoup

url = input("Enter the URL : ")
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup("a")
for tag in tags:
    print(tag.get("href", None))
