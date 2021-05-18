""" for testing the urllib library in python """

import urllib.request, urllib.parse, urllib.error
hand = urllib.request.urlopen("http://data.pr4e.org/intro-short.txt")
for line in hand:
    print(line.decode().strip())
