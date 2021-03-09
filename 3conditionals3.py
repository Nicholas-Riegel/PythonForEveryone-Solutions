#don't use arepl with this

def x():
    try:
        score = float(input('Enter score between 0 and 100: '))
        if score > 100 or score <= 0:
            print("Error")
        elif score >= 97:
            grade = 'A+'
        elif score >= 94:
            grade = 'A'
        elif score >= 90:
            grade = 'A-'
        elif score >= 87:
            grade = 'B+'
        elif score >= 84:
            grade = 'B'
        elif score >= 80:
            grade = 'B-'
        elif score >= 77:
            grade = 'C+'
        elif score >= 74:
            grade = 'C'
        elif score >= 70:
            grade = 'C-'
        elif score >= 67:
            grade = 'D+'
        elif score >= 64:
            grade = 'D'
        elif score >= 60:
            grade = 'D-'
        else:
            grade = 'F'
        print('Your grade is: '+grade)
    except:
        x()
x()
