n, k = map(int, input().split())

def C(a,b):
    if b == 0: return 1
    elif b > a: return 0
    else:
        return C(a-1,b) + C(a-1,b-1)

print(C(n,k))
