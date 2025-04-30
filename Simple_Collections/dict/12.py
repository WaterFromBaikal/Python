dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
dict3 = {}

dict3 = {**dict1, **dict2}
print(set(dict1.keys()).intersection(set(dict2.keys())))
print(dict1.keys() & dict2.keys())
for i in set(dict1.keys()).intersection(set(dict2.keys())):
    dict3[i] = [dict1[i], dict2[i]]
print(dict3)
print(type(dict1.keys()))

