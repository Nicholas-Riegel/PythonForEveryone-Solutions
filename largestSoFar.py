y = [9, 41, 12, 3, 74, 14]
z = y[0]
for x in y:
    if x > z:
        z = x
    print(z, x)
print('Largest:', z)

#smallest

q = y[0]
for p in y:
    if p < q:
        q = p
    print(q, p)
print('Smallest:', q)


smallest = None
print("Before:", smallest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar
    print("Loop:", itervar, smallest)
print("Smallest:", smallest)

smallest = None
for x in [9, 41, 12, 3, 74, 15]:
    if smallest is None:
        smallest = x
    elif x < smallest:
        smallest = x
    print(smallest, x)
print(smallest)