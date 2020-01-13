'''
if juila has j books and nancy has n. how many books do they have altogether?
convert and print as roman numbers
j and n are user entered value
'''
romansValues=[(1000,'M'),(900,'CM'),(500,'D'),(400,'CD'),(100,'C'),(90,'XC'),
        (50,'L'),(40,'XL'),(10,'X'),(9,'IX'),(5,'V'),(4,'IV'),(1,'I')]

def convRoman(num):
    romans=''
    while num>0:
        for i,k in romansValues:
            while num>=i:
                romans+=k
                num-=i
    return romans

print(convRoman(9))