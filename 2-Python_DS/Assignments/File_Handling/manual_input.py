
fname = input('Enter the filename you want to open: ')
try:
    fhand = open(fname)
except FileNotFoundError:
    print('File', fname, 'is not found')
    quit()
count = 0
character = input('Enter the first character of the line you want to display: ')
for line in fhand:
    line = line.strip()
    if line.startswith(character):
        count = count+1
print('There are', count, 'subject lines in', fname, 'that starts with', character)