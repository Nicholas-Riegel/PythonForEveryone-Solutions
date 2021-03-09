score = float(input('Enter score between 0 and 1: '))
if score >= 1 or score <= 0:
    print("Error")
elif score >= .9:
    print('A')
elif score >= .8:
    print('B')
elif score >= .7:
    print('C')
elif score >= .6:
    print('D')
else:
    print('F')
