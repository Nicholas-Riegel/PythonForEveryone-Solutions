import re

name = input('Enter file name: ')
if len(name) == 0:
    name = 'mbox-short.txt'

handle = open(name)

list0 = list()
list1 = list()

for x in handle:
    y = re.findall('^New Revision: ([0-9.]+)', x)
    if len(y) < 1: continue
    list0 += y

for z in list0:
    list1.append(float(z))

print(sum(list1) / len(list1))