count = int(input())
class_hierarchy = {'object':[]}
for i in range(count):
    src1 = input()
    if len(src1) == 1:
        class_hierarchy['object'].append(src1)
    else:
        src2 = src1.replace(' ', '').split(sep=':')
        if src2[1] not in class_hierarchy:
            class_hierarchy[src2[1]] = []
        class_hierarchy[src2[1]].append(src2[0])

print(class_hierarchy)

# a = 'a : b'
# b = a.replace(' ', '').split(sep=':')
# print(b)

# class_hierarchy = {'object':['A', 'B', 'L'], 'L':['K'], 'A':['C','D'], 'B':['E'], 'C':['F'], 'D':['G'], 'E':['H'], 'F':['I'], 'G':['I'], 'H':['J'], 'I':['K']}
# def isPredok(a,b):
#
#     if a == b:
#         return True
#     elif b in class_hierarchy[a]:
#             return True
#     else:
#         parents_list = [key for key,value in class_hierarchy.items() if b in value]
#         for i in parents_list:
#             if isPredok(a, i):
#                 return True
#
#
# print(isPredok('A', 'K'))