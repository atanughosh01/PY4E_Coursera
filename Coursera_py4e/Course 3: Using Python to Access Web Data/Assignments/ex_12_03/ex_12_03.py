""" In this assignment you will write a Python program that expands on http://www.py4e.com/code3/urllinks.py.
The program will use urllib to read the HTML from the data files below, extract the href= values from the
anchor tags, scan for a tag that is in a particular position relative to the first name in the list,
follow that link and repeat the process a number of times and report the last name you find.
DATA : http://py4e-data.dr-chuck.net/known_by_Bob.html """

# importing necessary packages
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Enter http://py4e-data.dr-chuck.net/known_by_Bob.html as URL
url = input("\nEnter URL : ")                               # prompts user for the URL on which scrapping is to be done
try:                                                        # try to convert variables to integer // type-casting
    repeat_count = int(input("Enter Repetition Count : "))  # prompts user for the number of repetition of scrapping
    pos = int(input("Enter Position : ")) - 1               # prompts user for the position from which data is to be scrapped
except ValueError:                                          # catch ValueError exception upon type-casting failure
    print("Error ! Please Enter Numeric Value(s)")          # display error message to enter numeric data
    quit()                                                  # quits the program execution

for i in range(repeat_count):                               # do until repetition count != 0
    html = urllib.request.urlopen(url, context=ctx).read()  # open the url (comprising of HTML) // similar to open() in file-handling
    soup = BeautifulSoup(html, "html.parser")               # defininng the method / function which parses specific HTML tag(s)
    tags = soup("a")                                        # parses all HTML anchor (<a></a>) tags
    link = tags[pos].get("href", None)                      # extract the href attributes of the anchor tags // extract links
    url = link                                              # assign the extracted link to url for re-extraction in the next iteration
    print("\nRetrieving :", link)                           # display the extracted link / href_attr in each iteration
    name = tags[pos].contents[0]                            # extract the tag name // extract our desired output
    print("Name Found :", name)                             # display the extracted tag name
