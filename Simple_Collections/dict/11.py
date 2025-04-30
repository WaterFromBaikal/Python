src = 'hello world hello'
result_dict = {}
for i in src.split():
    if i not in result_dict:
        result_dict[i] = 1
    else:
        result_dict[i] += 1
print(result_dict)