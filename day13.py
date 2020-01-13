'''
kara and lina are selling lemonade. kara sells with 5 rs a glass and lina sells 7 rs a glass
calculate total glass sold by both. and display who made highest money.
no of glass sold is user entered value
'''

kara=5
lina=7
ksold=int(input('enter sold quantity of kara'))
lsold=int(input('enter sold quantity of lina'))

totalk=ksold*kara
totall=lsold*lina
# print('kara made',totalk,'rs')
# print('lina made',totall,'rs')
if totall>totalk:
    print('lina made more money than kara ,that is',totall)
elif totalk>totall:
    print('kara made more money than lina ,that is', totalk)
else:
    print('both made equal money')