a = int(input())
dict_of_namespace = {'global' :
                         {'variables':set(),
                          'parent':'none'}
                     }
list_of_input = []
for i in range(a):
    list_of_input.append(input().split())


def getNamespace(namespace, var):
    if namespace not in dict_of_namespace:
        print('No namespace')
        return

    if var in dict_of_namespace[namespace]['variables']:
        print(namespace)
    elif dict_of_namespace[namespace]['parent'] == 'none':
            print('None')
    else: getNamespace(dict_of_namespace[namespace]['parent'], var)

for src in list_of_input:
    
    operation = src[0]

    if operation == 'add':
        namespace = src[1]
        var = src[2]
        dict_of_namespace[namespace]['variables'].add(var)
    elif operation == 'create':
        namespace = src[2]
        var = src[1]
        dict_of_namespace[var] = {'variables': set(), 'parent': namespace}
    elif operation == 'get':
        namespace = src[1]
        var = src[2]
        getNamespace(namespace, var)
