'''
write a program that for a given hour and minutes values calculates an angle in
degrees between the  hr and the min hands. check whether the min hand overlapping
the hr hand at a given time.
'''
def angleCalc(h,m):
    if h<0 or h>12 or m<0 or m>60:
        print('please enter correct input')
    if h==12:
        h=0
    if m==60:
        m=0
    hourAngle=0.5*(h*60+m)
    minAngle=6*m
    angle=abs(hourAngle-minAngle)
    angle=min(360-angle,angle)
    return int(angle)

h=int(input('enter hr(0-12)'))
m=int(input('enter min(0-59)'))

clockangle=angleCalc(h,m)
if clockangle==0:
    print('hour and minute hands overlap')
else:
    print('clock angle is',clockangle)

