'''
the no of red blood corpuscles in one the cubic milimetre is about 500000 and the no of white
blood corpuscles in one cubic milimeter is about 8000. what then s the ratio of white
blood corpuscles to red blood corpuscles?Aspect ratio should be as int value
'''
# red=5000000
# white=8000
# calcred=white/white
# calcwhite=red/white
# print(int(calcred),':',int(calcwhite))

def greatestCommonFactor(white,red):
    return white if red==0 else greatestCommonFactor(red,white%red)
red=5000000
white=8000
factor=greatestCommonFactor(white,red)

whiteRatio=int(white/factor)
redRatio=int(red/factor)
print('Aspect ratio',whiteRatio,':',redRatio)

