'''
7.1 Write a program that prompts for a file name, then opens that file and
reads through the file, and print the contents of the file in upper case.
Use the file words.txt to produce the output below.
You can download the sample data at http://www.py4e.com/code3/words.txt
'''

# Use words.txt as the file name

fname = input("Enter file name: ")  # prompting user for input
fname = fname.strip()  # removing whitespaces and '/n'-s from starting and ending

try:
    fhand = open(fname)  # opening the file chosen by user
except FileNotFoundError:  # catching exception if no such file is found
    print('File', fname, 'is not found')
    quit()

inp = fhand.read()  # reads text from file as a whole string
upper_case = inp.upper()  # returns a copy of the string converted to uppercase
print(upper_case)  # prints the uppcase text
