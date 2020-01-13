'''
baachu, bogra, thipra,rajju
print all possible combinations
'''
def printCombi(array):
    if len(array)==0:
        return []
    if len(array)==1:
        return [array]
    l=[]
    for i in range(len(array)):
        print('i-->',i)
        m=array[i]
        print('--m',m)

        remlst=array[:i]+array[i+1:]
        print('remlist==',remlst)

        for p in printCombi(remlst):
            print('p---',p)
            print('==l',l)
            l.append([m]+p)
            print('AFTER==l', l)


    return l

students=['a', 'b', 'c','d']

for i in printCombi(students):
    print(i)
