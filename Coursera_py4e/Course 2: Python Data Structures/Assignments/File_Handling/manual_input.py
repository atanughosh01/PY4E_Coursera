
fname = input('Enter the filename you ant to open = ')
try:
    fhand = open(fname)
except FileNotFoundError:
    print('File',fname,'is not found')
    quit()
count = 0
for line in fhand:
    line = line.strip()
    if line.startswith('I '):
        count = count+1
print('There are',count,'subject lines in',fname,'that starts with "I"')