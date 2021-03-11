total = 0
count = 0
while True:
    answer = input("Enter a number or type 'done': ")
    if answer == 'done':
        break
    else:
        try:
            x = float(answer)
        except:
            print('Invalid input')
            continue
        total += x
        count += 1
print(total, count, total/count)