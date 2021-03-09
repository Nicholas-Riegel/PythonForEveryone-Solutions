try:
    h = float(input('Enter Hours: '))
except:
    print('Error, please enter numeric input')
    quit()
try:
    r = float(input('Enter rate per hour: '))
except:
    print('Error, please enter numeric input')
    quit()

if h > 40:
    pay = (40*r)+((h-40)*(r*1.5))
else:
    pay = h * r
print('Your total pay is: $'+str(pay))
