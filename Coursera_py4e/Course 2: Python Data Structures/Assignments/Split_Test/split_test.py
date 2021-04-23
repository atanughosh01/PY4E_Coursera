""" program to test the split() function after reading text from
a .txt file """

file = input('Enter file name: ')
fhand = open(file)

for line in fhand:
    line = line.rstrip()
    if not line.startswith('From'):
        continue
    words = line.split()
    print(words[0])