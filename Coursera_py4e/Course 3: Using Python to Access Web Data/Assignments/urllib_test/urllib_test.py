""" for testing the urllib library in python """

import urllib.request, urllib.parse, urllib.error
hand = urllib.request.urlopen("http://data.pr4e.org/intro-short.txt")
print("")
for line in hand:
    print(line.decode().strip())

print("\n----------------------------------------------------\n")

file_hand = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")
counts = dict()
for lines in file_hand:
    print(lines.decode().strip())
    words = lines.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print("")
for x, y in ([(k, v) for k, v in counts.items()]):
    print("Word :", x, ", Count :", y)
