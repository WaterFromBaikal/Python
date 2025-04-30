# 1
a = set()
for i in range(1,11):
    a.add(i)
print('#1')
print(a)
# 2
a.add(11)
print('#2')
print(a)
# 3
a.discard(5)
print('#3')
print(a)
# 4
print('#4')
print(8 in a)
# 5
print('#5')
b = set()
for i in range(5, 15):
    b.add(i)

# 6
print('#6')
print(a.intersection(b))
a1 = {1,2,3,4}
b1 = {1,3}
c1 = {1,2}
print(a1.intersection(b1,c1))
print(a1.difference(b1,c1))

# 7
print('#7')
print(a.union(b))

# 8
print('#8')
print(a)
print(b)
print(a.difference(b))
# 9
print('#9')
a.clear()
print(a)
# 10
print('#10')
a = {1,2,3,4}
b = {3,4,5,6}
# print(type(a))
def sim_dif(a,b):
    if isinstance(a, set) and isinstance(b,set):
        return a.symmetric_difference(b)


print(sim_dif(a, b))