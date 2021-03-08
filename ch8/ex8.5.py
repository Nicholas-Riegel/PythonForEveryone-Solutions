fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
count = 0
for x in fh:
    x = x.rstrip()
    if not x.startswith('From '):
        continue
    lst = x.split()
    print(lst[1])
    count += 1
print("There were", count, "lines in the file with From as the first word")
