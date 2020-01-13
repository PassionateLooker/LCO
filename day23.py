'''
convert int value to binary
'''
# a=2
# print(bin(a))

def decToBin(val):
    bal=''
    while val!=1:
        x=str(val%2)
        bal+=x
        val=val//2
    return '1'+bal

print(decToBin(4))
