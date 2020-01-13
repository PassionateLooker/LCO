'''
find max of these elements
1,0,5,4,2,7,465,4
without using conditional statements and loops
'''
array=[0,45,2,6,1,8]
def largest(n):
    n.sort()
    l=n[-1]
    return l
print(largest(array))