mu = 178
sigma = 9

values = [169, 187, 160, 196]

print("Normeeratut lukuarvot:")
for x in values:
    z = (x - mu) / sigma
    print(f"{x} cm -> z = {z:.3f}")
