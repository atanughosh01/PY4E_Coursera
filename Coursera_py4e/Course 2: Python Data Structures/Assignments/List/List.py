# following two code snippets works almost the same

print('-----------------------------')

total = 0.0
count = 0
while True:
    inp = input('Enter a value: ')
    if inp == 'done':
        break
    num = float(inp)
    total += num
    count += 1
Average = total/count
print('Average =', Average)

print('-----------------------------')

numlist = list()
while True:
    inp = input('Enter a value: ')
    if inp == 'done':
        break
    num = float(inp)
    numlist.append(num)
Average = sum(numlist)/len(numlist)
print('Average =', Average)

print('-----------------------------')
