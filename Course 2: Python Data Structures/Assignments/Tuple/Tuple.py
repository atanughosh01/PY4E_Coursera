# implementation of Tuple data structure
print('-------------------------------------')

# sort a tuple (default by values)
dic = {'a': 1, 'c': 12, 'b': 100}
z = dic.items()
print(z)
k = sorted(z)
print('Key Sorted :', k)
for x, y in k:
    print(x, y)
print('-------------------------------------')

# sort a tuple by key (not value)
dic = {'a': 1, 'c': 12, 'b': 100}
lst = list()
for k, v in dic.items():
    lst.append((v, k))
print(lst)
new_lst = sorted(lst, reverse=True)
print('Value Sorted :', new_lst)
for x, y in new_lst:
    print(x, y)
print('-------------------------------------')
