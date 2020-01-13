'''
a program to check whether a string is valid password
-atleast one number
-atleast 1 upper and lowercase letter
-atleast 1 special symbol
-should be between 6 to 20 character long
'''
def pass_check(passwd):
    specialSymbol=['$','@','#','%']
    val=True

    if len(passwd)<6:
        print('length should be atleast 6 digits long')
        val=False
    if len(passwd)>20:
        print('length of passwd should not be more than 20')
        val=False

    if not any(char.isdigit() for char in passwd):
        print('passwd should have atleast 1 digit')
        val=False
    if not any(char.isupper() for char in passwd):
        print('passwd should have atleast 1 uppercase')
        val=False
    if not any(char.islower() for char in passwd):
        print('passwd should have atleast 1 lowercase')
        val=False

    if not any(char in specialSymbol for char in passwd):
        print('passwd should have atleast 1 special character')
        val=False

    if val:
        return val



password=input('enter password')
if pass_check(password):
    print('password is valid')
else:
    print('password is invalid')