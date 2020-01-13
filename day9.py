'''
Day 9 Challenge:
Mr Richard Tupper is purchasing gifts for him
family. So far he has purchased the following:
3 sweaters, each valued at $68
1 computer game valued at $75
2 bracelets, each valued at $43
Later, he returned one of the bracelets for a full

refund and received a $10 rebate on the com
puter game. What is the total cost of the gifts

after refund and rebate?
Calculation part of the program should be under three lines.
'''
sweaters=68
computergame =75
bracelets=43

sweaterCount=3
computergameCount=1
braceletCount=2

returned=1
rebate=10

totalGiftPrice=sweaters*sweaterCount+computergame*computergameCount+bracelets*braceletCount
discountAndRebate=bracelets*returned+rebate

totalDiscount=totalGiftPrice-discountAndRebate
print('Final gift price is',totalDiscount)
