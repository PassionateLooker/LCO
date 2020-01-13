'''
program that accepts 2 numbers from user and then prints the sum, difference,product,avg ,max and min
'''

number1=int(input('enter number1: '))
number2=int(input('enter number2: '))
print('sum of',number1,'and',number2,'is',number1+number2)
print('sub of',number1,'and',number2,'is',number1-number2)
print('mul of',number1,'and',number2,'is',number1*number2)
print('avg of',number1,'and',number2,'is',(number1+number2)/2)
print('max of',number1,'and',number2,'is',max(number1,number2))
print('min of',number1,'and',number2,'is',min(number1,number2))