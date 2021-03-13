list = [1, 2, 3, 4, 5]

# def chop(x):
#     del x[0]
#     del x[len(x) - 1]
    
# print(chop(list))
# print(list)

def middle(x):
    return x[1:len(x)-1]

print(middle(list))
print(list)