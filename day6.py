'''
A floppy disk shows f bytes free and u bytes used. if you delete a file of size o bytes and
create a new file of size n bytes,how many free bytes will the floppy disk have?
f u o and n are user entered values
'''

f=int(input('enter disk size'))
u=int(input('enter file used size'))
o=int(input('enter deleted file size'))
n=int(input('enter new file size'))
totalSize=f+u
afterDelete=totalSize-o
afterAdd=afterDelete-n

print('free size is ',afterAdd)

