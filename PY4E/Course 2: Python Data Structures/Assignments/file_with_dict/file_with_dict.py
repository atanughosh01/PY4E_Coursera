""" Program to read text from a file given as user input and
finding out the word with most number of appearances and the
number of times it is present in that file """

file_name = input('Open File: ')    # prompts user for file name
try:                                # tries to open the file
    file_handler = open(file_name)  # opens the file chosen by user
except FileNotFoundError:           # catches exception if no such file is found
    print('File', file_name, 'is not found')
    quit()                          # quits the program

counts = dict()                     # creating an empty dictionary to store the words present in file
for line in file_handler:           # hovering through all the lines present in the file
    words = line.split()            # reads through lines, splits them into words & stores in a list() named as 'words'
    for word in words:              # hovering through all the word-s present in the list 'words'
        counts[word] = counts.get(word, 0) + 1
# increment the count of an 'word' if it is already present in the dict()
# else if the 'word' absent in the dict(), add it to the dict()
# '0' is the default count if no such 'word' is present in the dict()

largest_count = None                # initialising number of appearances of the word with most appearances to NULL
word_with_most_count = None         # initialising the word with most number of appearances to NULL
count_list = counts.items()         # creates a list() of the words along with their counts as (key, value) pair
for word, count in count_list:      # hovering through the list() of word-s along with their counts
    # conditional statement to check which word has the most number of appearances and how many times it appeared
    if largest_count is None or count > largest_count:
        word_with_most_count = word
        largest_count = count

# displaying the result
print('The word with most appearances :-', word_with_most_count)
print('Number of times that word appeared :-', largest_count)
