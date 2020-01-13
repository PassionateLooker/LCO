'''
sort using bubble sort

'''

a=[2,6,4,8,9,1]
l=len(a)
for i in range(l):
    for j in range(l-i-1):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
print(a)







