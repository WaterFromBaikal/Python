# 1
a = ('aa','bb','cc', 'apple')
# 2
print(a[0])
# 3
d,b,c,c1 = a
print(a,b,c)
# 4
# a[0] = 'test'
# 5
b = (a)
print(b)
# 6
e = ('1','2','3')
f = a + e
print(f)
g = f[5:2:-1]
print(g)
# 7
print('apple' in a)
# 8
print(len(a))
# 9
print(a)
a_list = list(a)
a_list[0] = 'new_val'
a_list_tuple = tuple(a_list)
print(a_list_tuple)

# 10
def multiple_tuple(a):
    mult = a[0]
    for i in range(1,len(a)):
        mult*=a[i]
    return mult

test = (1,2,3,4,5,6)
print(multiple_tuple(test))