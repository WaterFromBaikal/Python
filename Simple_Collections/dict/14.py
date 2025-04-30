from Stepik.Simple_Collections.list.Task1 import value

data = {"a": 10, "b": 20, "c": 20}

def max_val_by_key(a):
    max_val = max(a.values())
    if isinstance(a, dict) and all(isinstance(i, (int, float)) for i in a.values()):
    #     for key, value in a.items():
    #         if value == max_val:
    #             result.append(key)
    # return result
        return [key for key, value in a.items() if value ==max_val]


print(max_val_by_key(data))

