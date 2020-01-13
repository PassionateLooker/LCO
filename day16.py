'''
write a prog to get sum of n nums.
ex: sum of 132 is 6
n is user entered value
'''

def getSum(n):
    total=0
    while n>0:
        dig=n%10
        # print(dig)
        total+=dig
        # print(total)
        n=n//10
        # print(n)
    return total

n=int(input('enter no'))
print(getSum(n))