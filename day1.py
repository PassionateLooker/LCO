'''there was a teacher in a small town who loves coding and he wants to create a program
which prints out the whole multiplication table of an entered number for his students.
write a program.
'''
def mul(n,till):
    for i in range(1,till+1):
        print(n,'X',i,'=',n*i)

mul(2,15)