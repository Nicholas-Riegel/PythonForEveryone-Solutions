largest = None
smallest = None

while True:
    num = input("Enter a number or 'done': ")
    if num == "done":
        break
    else:
        try:
            num = int(num)
            if largest is None:
                largest = num
            elif num > largest:
                largest = num
            if smallest is None:
                smallest = num
            elif num < smallest:
                smallest = num
        except:
            print('Invalid input')

print('Maximum is', largest)
print('Minimum is', smallest)