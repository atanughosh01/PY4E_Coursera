""" 8.4 Open the file romeo.txt and read it line by line.
For each line, split the line into a list of words using the
split() method. The program should build a list of words. For
each word on each line check to see if the word is already in the
list and if not append it to the list. When the program completes,
sort and print the resulting words in alphabetical order.
You can download the sample data at http://www.py4e.com/code3/romeo.txt """

fname = input("Enter file name: ")          # prompts user for file name
try:                                        # tries to open the file
    fhand = open(fname)                     # opens the file chosen by user
except FileNotFoundError:                   # catches exception if no such file is found
    print('File', fname, 'is not found')    # displays error message
    quit()                                  # quits the program
lst = list()                                # creates an empty list for the desired output
for line in fhand:                          # reads every line of the given file
    line = line.rstrip()                    # removes whitespaces from end of the lines
    wordList = line.split()                 # splits the line into a list of words
    for element in wordList:                # checks every element in the word list
        if element in lst:                  # if any element is repeated
            continue                        # does nothing
        else:                               # else if certain element is not present in the list
            lst.append(element)             # appends the element in the list
# de-indentation indicates that sorting is done when the loop ends
lst.sort()                                  # sorts the list in alphabetical order of starting characters
print(lst)                                  # prints the list
