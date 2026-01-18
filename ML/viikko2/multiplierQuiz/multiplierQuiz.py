import random

kerrat = 5
x = []
y = []
tulo = []
vastaus = []

def numberGen():
    i = 0
    while i < kerrat:
        x.append(random.randrange(1,10))
        y.append(random.randrange(1,10))
        tulo.append(x[i] * y[i])
        i += 1

def questions():
    i = 0
    while i < kerrat:
        vastaus.append(int(input(f"{x[i]} * {y[i]} = ")))
        i += 1

def answers():
    i = 0
    oikein = 0
    while i < kerrat:
        if tulo[i] == vastaus[i]:
            print(f"Oikein :-) {x[i]} * {y[i]} = {tulo[i]}")
            oikein += 1
        else:
            print(f"Väärin :-( {x[i]} * {y[i]} = {tulo[i]}")
        i += 1
    print(f"Sait {oikein} oikein!")

numberGen()
questions()
answers()