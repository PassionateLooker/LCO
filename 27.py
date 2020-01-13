'''
convert centimeter to inch ,meter and kilometer
'''

centimeter=int(input('enter centimeter value'))
convToInch=centimeter/2.54
convToMeter=centimeter/100
convToKilometer=centimeter/100000
#OR
# convToInch=centimeter*0.394
# convToMeter=centimeter*0.01
# convToKilometer=centimeter*0.00001

print(centimeter,'centimeter in inch is',convToInch)
print(centimeter,'centimeter in meter is',convToMeter)
print(centimeter,'centimeter in kilometer is',convToKilometer)