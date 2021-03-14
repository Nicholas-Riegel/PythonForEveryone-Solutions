fhand = open('words.txt')
dict = dict()
for x in fhand:
    x = x.rstrip()
    list = x.split()
    for y in list:
        dict[y] = 1
print(dict)

if 'Writing' in dict:
    print("'Writing' is in dict")