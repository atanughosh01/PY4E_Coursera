"""These two code snippets are almost equivalent"""

print('--------------------------------------------------')

# counts = {'atanu':1, 'x':2, 'abc':23, 'y':100, 'z':69}
counts = dict()
names = ['atanu', 'akash', 'apurba', 'sayan']
for name in names:
    if name in counts:
        counts[name] += 1
    else:
        counts[name] = 0
print(counts)

print('--------------------------------------------------')

# counts = {'atanu':1, 'x':2, 'abc':23, 'y':100, 'z':69}
counts = dict()
names = ['atanu', 'akash', 'apurba', 'sayan']
for name in names:
    counts[name] = counts.get(name, 0)
print(counts)

print('--------------------------------------------------')
