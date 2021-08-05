
fhand = open('readthis.txt')
count = 0
for line in fhand:
    line = line.strip()
    if not line.startswith('I'):
        print(line)
    count = count+1
print('Number of Lines =', count)
