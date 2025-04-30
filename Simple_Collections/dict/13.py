numbers = [1, 2, 3, 4, 5, 6]
result = {0:[],1:[],2:[]}


for i in numbers:
    result[i%3].append(i)
print(result)
