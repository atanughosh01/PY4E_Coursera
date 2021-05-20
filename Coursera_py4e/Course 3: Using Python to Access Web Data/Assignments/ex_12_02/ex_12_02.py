""" Scraping Numbers from HTML using BeautifulSoup In this assignment
you will write a Python program similar to http://www.py4e.com/code3/urllink2.py.
The program will use urllib to read the HTML from the data files below, and parse
the data, extracting numbers and compute the sum of the numbers in the file.
DATA : http://py4e-data.dr-chuck.net/comments_1189778.html """

# importing necessary packages
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# enter http://py4e-data.dr-chuck.net/comments_1189778.html as URL
url = input("\nEnter URL : ")                             # prompts user for the URL on which scrapping is to be done
html = urllib.request.urlopen(url, context=ctx).read()  # open the url (comprising of HTML) // similar to open() in file-handling
soup = BeautifulSoup(html, "html.parser")               # defininng the method / function which parses specific HTML tag(s)

# Retrieve all of the span tags
tags = soup("span")                                     # parses all HTML span (<span></span>) tags
content_list = list()                                   # create an empty list to store the contents / numbers
for tag in tags:
    # look at the parts of a tag
    print("\nTAG :", tag)
    print("CLASS NAME LIST :", tag.get("class", None))
    print("CLASS NAME :", tag.get("class", None)[0])
    print("CONTENT LIST :", tag.contents)               # parse and get the number list
    print("CONTENT :", tag.contents[0])                 # parse and get the numbers
    print("ATTR :", tag.attrs)
    for i in tag.contents:
        content_list.append(int(tag.contents[0]))       # store the numbers to the list

# displays the final result(s)
print("\nList of Numbers :", content_list)
print("\nCount of Numbers in the List =", len(content_list))
print("\nSum of Numbers in the List =", sum(content_list))
