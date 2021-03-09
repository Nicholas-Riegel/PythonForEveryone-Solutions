fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print('File not found')
    quit()
lst = list()
for line in fh:
    line = line.rstrip()
    list1 = line.split()
    for x in list1:
        if not x in lst:
            lst.append(x)
lst.sort()
print(lst)