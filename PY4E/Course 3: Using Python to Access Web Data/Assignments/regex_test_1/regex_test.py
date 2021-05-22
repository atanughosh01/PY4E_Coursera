""" for testing regular expression"""

import re
fhand = open("mbox-short.txt")
num_list = list()

print("\nThe Confidence Values are :", end=" ")
for line in fhand:
    line = line.rstrip()
    stuff = re.findall("^X-DSPAM-Confidence: ([0-9.]+)", line)
    if len(stuff) != 1: continue
    # print(stuff)
    num = float(stuff[0])
    print(stuff[0], " ", end=" ")
    num_list.append(num)

print("\n\nThe Maximum Confidence Value is :", max(num_list))
