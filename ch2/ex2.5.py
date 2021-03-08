x = input('Enter Celsius: ')
try:
    y = float(x)
except:
    print('Not a number')
    quit()
z = y*1.8 + 32
print(z, 'Farenheit')