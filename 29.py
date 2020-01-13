'''
write a program to take the user for a distance(in meters) and the time was taken(as 3 number:hrs,min and seconds)
and display the speed in miles per hour
'''
distance=float(input('enter distance in meters'))
hr=float(input('input hours'))
minute=float(input('enter minutes'))
sec=float(input('enter seconds'))

timesecs=(hr*3600)+(minute*60)+sec
kph=(distance/1000.0)/(timesecs/3600.0)
mph=kph/1.609

print('your speed in miles/h is',mph)