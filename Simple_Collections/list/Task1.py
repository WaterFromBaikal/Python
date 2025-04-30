# 1
a = []
for i in range(1,11):
    a.append(i)

print(a)
# 2
a.append(11)
print(a)
# 3
a.append(5)
for i in a:
    if i == 5:
        a.remove(5)
        break
print(a)
# 4
a[1] = 99
print(a)

# 5
a.append(7)
for index,value in enumerate(a):
    if value == 7:
        print(index, end=' ')
index_of_seven_in_a = [index for index, value in enumerate(a) if value == 7]
print(*index_of_seven_in_a)
# 6
print(8 in a)
# 7
print(a)
a.sort()
print(a)
a.sort(reverse=True)
print(a)

# 8
nechet = [var for var in a if var%2==1]
print(nechet)

# 9
count = 0
for i in nechet:
    count+=i
print(count)

print(sum(nechet))

#10

def list_to_reverse(a):
    return sorted(a)
print(a)
print(list_to_reverse(a))