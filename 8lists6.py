list = list()
while True:
    x = input("Enter number or 'done': ")
    if x == 'done':
        break
    else:
        try:
            x = float(x)
        except:
            print("Input neither a number nor 'done'.")
            continue
        list.append(x)

print('Maximum:', max(list))
print('Minimum:', min(list))