""" 8.5 Open the file mbox-short.txt and read it line by line.
When you find a line that starts with 'From ' like the following line:
From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
You will parse the From line using split() and print out the second word
in the line (i.e. the entire address of the person who sent the message).
Then print out a count at the end. Hint: make sure not to include the
lines that start with 'From:'. Also look at the last line of the sample
output to see how to print the count.
You can download the sample data at http://www.py4e.com/code3/mbox-short.txt """

fname = input("Enter file name: ")              # prompts user for file name
# guardian/conditional statement to avoid absurd filenames
if len(fname) < 1:                              # if absurd filename taken as input
    fname = "mbox-short.txt"                    # considers filename as "mbox-short.txt"
else:                                           # else if proper filename taken as input
    try:                                        # tries to open the file
        fhand = open(fname)                     # opens the file chosen by user
    except FileNotFoundError:                   # catches exception if no such file is found
        print('File', fname, 'is not found')    # displays error message
        quit()                                  # quits the program
count = 0                                       # initialise the line count
for line in fhand:                              # reads every line of the given file
    if line.startswith('From '):                # if line starts with 'From ' element
        lne = line.rstrip()                     # removes whitespaces from end of the lines
        wordList = line.split()                 # splits the line into a list of words
        print(wordList[1])                      # prints out the second word from each lines
        count += 1                              # increments the count wrt number of lines
# displays number of lines stating with 'From ' element
print("There were", count, "lines in the file with From as the first word")