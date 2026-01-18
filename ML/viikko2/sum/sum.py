import random

def printSum(x,y):
    summa = x + y
    print(f"Lukujen {x} ja {y} summa on: {summa}")
    
a = random.randrange(1,10)
b = random.randrange(1,10)
printSum(a,b)