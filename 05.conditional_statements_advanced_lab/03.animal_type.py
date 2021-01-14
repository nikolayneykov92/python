animal = input()

isMammal = animal == 'dog'
isReptile = animal == 'crocodile' or animal == 'tortoise' or animal == 'snake'

if isMammal:
    print('mammal')
elif isReptile:
    print('reptile')
else:
    print('unknown')
