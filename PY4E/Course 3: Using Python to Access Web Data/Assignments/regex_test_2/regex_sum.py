"""sum of numbers from a .txt file"""

import re
try:
    hand = open("regex_sum_42.txt")
except FileNotFoundError:
    print("Error ! File not found")
    quit()

print("\nThe numbers present in the file are :", end=" ")
num_list = list()

for line in hand:
    line = line.strip()
    stuff = re.findall("[0-9]+", line)
    for j in stuff:
        num_list.append(float(j))
        print(" ", j, end=" ")

print("\n\nCount of the numbers present in the file =", len(num_list))
print("\nSum of the numbers present in the file =", int(sum(num_list)))
