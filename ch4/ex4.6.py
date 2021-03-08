
h = float(input('Enter Hours: '))
r = float(input('Enter rate per hour: '))

def computePay(hours, rate):
    if hours > 40:
        pay = (40*rate)+((hours-40)*(rate*1.5))
    else:
        pay = hours * rate
    return pay

pay = computePay(h, r)

print('Pay: $'+str(pay))
