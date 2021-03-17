import re

hand = open('regex_sum_1178892.txt')

list0 = list()
list1 = list()

for x in hand:
    y = re.findall('[0-9]+', x)
    if len(y) < 1: continue
    list0 += y

for z in list0:
    num = float(z)
    list1.append(num)

print(sum(list1))