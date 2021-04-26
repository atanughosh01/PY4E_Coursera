# implementation of Dictionary data structure

# counts = {'atanu':1, 'x':2, 'abc':23}
counts = dict()
names = ['atanu', 'x', 'y', 'z']
for name in names:
    if name in counts:
        counts[name] += 1
    else:
        counts[name] = 1
print('The dictionary is :', counts)