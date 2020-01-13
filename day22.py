'''
find leap year
'''

year=int(input('enter a year'))
print('leap year' if year%400==0 else 'leap year'if year%4==0 and year%100!=0 else
'non leap year')
