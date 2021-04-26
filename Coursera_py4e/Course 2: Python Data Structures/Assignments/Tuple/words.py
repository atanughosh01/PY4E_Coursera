"""program to find out top 10 common words (most appearances) from a file"""

file_name = input('Open File: ')
try:
    file_handler = open(file_name)
except FileNotFoundError:
    print('File', file_name, 'is not found')
    quit()

word_dict = dict()
for line in file_handler:
    word_list = line.split()
    for word in word_list:
        word_dict[word] = word_dict.get(word, 0) + 1
print('------------------------------------------------------------')

lst = list()
for k, v in word_dict.items():
    new_tuple = (v, k)
    lst.append(new_tuple)
new_lst = sorted(lst, reverse=True)

for v, k in new_lst[:10]:
    print('Word:', k, ',', 'Number of appearances:', v)
print('------------------------------------------------------------')

# shorter and better version of previous block
# this method is called 'LIST COMPREHENSION'
new_lst = sorted([(v, k) for k, v in word_dict.items()], reverse=True)

for v, k in new_lst[:10]:
    print('Word:', k, ',', 'Number of appearances:', v)
print('------------------------------------------------------------')
