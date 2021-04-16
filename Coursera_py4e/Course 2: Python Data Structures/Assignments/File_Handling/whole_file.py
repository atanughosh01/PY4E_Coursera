
# if we read this as a whole file
fhand = open('readthis.txt')
inp = fhand.read()
length = len(inp)
print('length of text file = ',length)
num = input('Enter upto which number, characters to be printed = ')
pos = int(num)
print(inp[:pos])