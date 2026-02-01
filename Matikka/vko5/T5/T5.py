mu = 178
sigma = 9

values = [180, 175, 185, 179]

print("Normeeratut lukuarvot:")
for x in values:
    z = (x - mu) / sigma
    print(f"{x} cm -> z = {z:.3f}")