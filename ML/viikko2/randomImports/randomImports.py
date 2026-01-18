import random

a = random.randrange(1,100)
print(f"numero a:{a}")
b = random.randrange(1,100)
print(f"numero b:{b}")
if a > b:
    print("a isompi")
elif a < b:
    print("b isompi")
else:
    print("yhtäsuuret")