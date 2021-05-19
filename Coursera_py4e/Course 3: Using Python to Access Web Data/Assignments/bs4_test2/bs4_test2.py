""" Scraping Numbers from HTML using BeautifulSoup In this assignment
you will write a Python program similar to http://www.py4e.com/code3/urllink2.py.
The program will use urllib to read the HTML from the data files below, and parse
the data, extracting numbers and compute the sum of the numbers in the file.
SAMPLE DATA : http://py4e-data.dr-chuck.net/comments_42.html """

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter URL : ")
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the span tags
tags = soup("span")
# print(tags)
content_list = list()
for tag in tags:
    # look at the parts of a tag
    print("\nTAG :", tag)
    print("CLASS NAME LIST :", tag.get("class", None))
    print("CLASS NAME :", tag.get("class", None)[0])
    print("CONTENT LIST :", tag.contents)
    print("CONTENT :", tag.contents[0])
    print("ATTR :", tag.attrs)
    for i in tag.contents:
        content_list.append(int(tag.contents[0]))

print("\nList of Numbers :", content_list)
print("\nCount of Numbers in the List =", len(content_list))
print("\nSum of Numbers in the List =", sum(content_list))
