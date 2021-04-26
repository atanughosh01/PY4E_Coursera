# implementation of Dictionary data structure
print('-------------------------------------------------')
# counts = {'atanu':1, 'x':2, 'abc':23}
counts = dict()
names = ['atanu', 'x', 'y', 'z']
for name in names:
    if name in counts:
        counts[name] += 1
    else:
        counts[name] = 1
print('The dictionary is :', counts)

print('-------------------------------------------------')

# program to check functionalities of dictionary DS
counts = {'atanu':1, 'x':2, 'abc':23, 'y':100, 'z':69}
print(list[counts])
print(counts.keys())
print(counts.values())
print(counts.items())

print('--------------------------------------------')

for name in counts:
    print('Key =', name, 'value =', counts[name])

print('--------------------------------------------')

for alpha, beta in counts.items():
    print('Key =', alpha, 'value =', beta)

print('--------------------------------------------')