import re

x = input('Enter Regular Expression: ')

handle = open('mbox.txt')

list0 = list()

for y in handle:
    z = re.findall(x, y)
    if len(z) < 1: continue
    list0 += z

print('mbox.txt had', len(list0), 'lines that matched', x)
