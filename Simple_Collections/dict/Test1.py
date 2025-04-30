# 1
from Stepik.Simple_Collections.list.Task1 import value

print('#1')
a = {}
b = {'a': 1, 'b': 2, 'c': 3, 'd':'name', 'e': 11, 'f':13}
print(type(a))
print(type(b))
# 2
print('#2')
a['d'] = '4'
print(a)
# 3
print('#3')
a['d'] = 4
print(a)

# 5
print('#5')
print('name' in a)
a['name'] = 'test'
print('name' in a)

# 6
print('#6')
print(a)
del a['name']
print(a)

# 7
print('#7')
print(type(b.values()))
print(type(b.keys()))

# 8
print('#8')

c = {}
print(type(c))
for key, value in b.items():
    print(f'{value} {type(value)}')
    if isinstance(value, int) and value > 10:
        c[key] = value
print(c)

# 9
print('#9')
a = {1:1, 2:2}
b = {3:3, 4:4}
c = {**a, **b, 0: 'default'}
print(c)

# 10
print('#10')
def dict_val_summ(a):
    sums = 0
    if isinstance(a, dict):
        for i in a.values():
            if isinstance(i, int):
                sums+=i
    return sums


print(dict_val_summ(c))
