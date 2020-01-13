'''
jack bought 400 hot dogs for the school picnic .if they were contained in packages of 8 hot
dogs,how many total packages did he buy? create python program without using \ ad % operator

'''
#print(divmod(400,8))<-----solution 1

totalHotDog=8
totalPerContainer=8
emptyContainer=0
while totalHotDog>=totalPerContainer:
    totalHotDog-=totalPerContainer
    emptyContainer+=1
print('jack bought total',emptyContainer,'containers')