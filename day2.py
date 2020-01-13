'''
print this pattern



        * *
        * *
      * * * *
      * * * *
    * * * * * *
    * * * * * *
  * * * * * * * *
  * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
'''

def patt(n):
    for i in range(1,n+1):

        k=i+1 if i%2!=0 else i
        for j in range(k,n):
            print(end=' ')
        for j in range(0,k):
            if j==k-1:
                print('*')
            else:
                print('*',end=' ')

patt(10)






