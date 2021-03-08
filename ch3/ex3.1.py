h = float(input('Enter Hours: '))
r = float(input('Enter rate per hour: '))

if h > 40:
    pay = (40*r)+((h-40)*(r*1.5))
else:
    pay = h * r
print('Your total pay is: $'+str(pay))
