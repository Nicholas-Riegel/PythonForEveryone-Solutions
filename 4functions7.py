def computegrade():
    try:
        score = float(input('Enter score between 0 and 1: '))
    except:
        print('Bad score')
        quit()
    if score >= 1 or score <= 0:
        print('Bad score')
        quit()
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

computegrade()
