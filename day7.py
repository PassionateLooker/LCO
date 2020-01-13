'''
The city bus system carries 1200000 people each day. how many people does the bus system
carry wach year? solve without using *,/,bitwise or loops
'''
def multiply(t,d):
    if d==0:
        return 0
    if d>0:
        return t+multiply(t,d-1)
    if d<0:
        return -multiply(t,d)
t=1200000
d=365
total=multiply(t,d)
print(total)

