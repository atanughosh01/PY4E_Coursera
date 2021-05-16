""" In this assignment you will read through and parse a
file with text and numbers. You will extract all the numbers
in the file and compute the sum of the numbers. """

import re                                           # import required packages
try:                                                # tries to open the file
    hand = open("regex_sum_1189776.txt")            # opens the chosen file
except FileNotFoundError:                           # catches exception if no such file is found
    print("\nError ! File not found")               # displays error message
    quit()                                          # quits the program
print("\nThe numbers present in the file are :", end=" ")

num_list = list()                                   # creates an empty list to store the numbers
for line in hand:                                   # hovering through the lines in the file handler
    line = line.strip()                             # removes whitespaces from both ends of line
    stuff = re.findall("[0-9]+", line)              # searches for all numbers in file and adds them to a list as string
    for j in stuff:                                 # hovering through the list of String(number)-s
        num_list.append(float(j))                   # convert String(num) --> float(num) and add them to the empty list
        print(" ", j, end=" ")                      # displays all numbers present in the file

# displays the final result
print("\n\nCount of the numbers present in the file =", len(num_list))
print("\nSum of the numbers present in the file =", int(sum(num_list)))
