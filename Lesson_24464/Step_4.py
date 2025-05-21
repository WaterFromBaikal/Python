class multifilter():
    def __init__(self, src:list, *funcs):
        self.src_list = src
        self.counter = 0
        self.funcs = [i for i in funcs]

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < len(self.src_list):
            tmp = self.src_list[self.counter]
            self.counter+=1
            return tmp
        else:
            raise StopIteration

    pos_count = 0
    neg_count = 0


a = list(range(11))



def mul2(x):
    return x % 2 == 0

def mul3(x):
    return x % 3 == 0

def mul5(x):
    return x % 5 == 0
result = []
b = multifilter(a,mul2, mul3, mul5)
for i in b:
    if mul2(i) or mul3(i) or mul5(i):
        result.append(i)
print(result)
