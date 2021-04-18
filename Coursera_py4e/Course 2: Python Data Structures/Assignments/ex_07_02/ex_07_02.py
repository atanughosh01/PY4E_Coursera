""" 7.2 Write a program that prompts for a file name, then opens that file and
reads through the file, looking for lines of the form: X-DSPAM-Confidence: 0.8475
Count these lines and extract the floating point values from each of the lines and
compute the average of those values and produce an output as shown below. Do not
use the sum() function or a variable named sum in your solution. You can download
the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing
below enter mbox-short.txt as the file name.
Match the output: Average spam confidence: 0.7507185185185187 """

# Use the file name mbox-short.txt as the file name

fname = input("Enter file name: ")  # prompting user for file name

try:
    fhand = open(fname)  # opening the file chosen by user
except FileNotFoundError:  # catching exception if no such file is found
    print('File', fname, 'is not found')
    quit()

# initializing count and total
total = 0.0
count = 0

for line in fhand:
    line = line.strip()  # removing whitespaces and '/n'-s from both ends of string

# finding the lines starting with 'X-DSPAM-Confidence:' and finding its ending position(s)
    if line.startswith("X-DSPAM-Confidence:"):
        print(line)
        pos = line.find(': ')  # finding position of the numeric substring
        # separating the numeric substring from char type
        line = line[pos+1:].strip()
        value = float(line)  # converting the numeric substring to float type

        # calculating the average
        total += value
        count += 1
        average = total / count

# displaying the final output
print("Average spam confidence:", average)
