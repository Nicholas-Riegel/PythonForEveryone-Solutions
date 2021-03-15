'''
Exercise 3: Write a program that reads a file and prints the letters in decreasing order of frequency. Your program should convert all the input to lower case and only count the letters a-z. Your program should not count spaces, digits, punctuation, or anything other than the letters a-z. Find text samples from several different languages and see how letter frequency varies between languages. Compare your results with the tables at https://wikipedia.org/wiki/Letter_frequencies.

'''
import string

name = input("Enter file: ")
if len(name) < 1:
    name = "mbox-short.txt"

try:
    handle = open(name)
except:
    print('File not found')
    quit()

dict1 = dict()

for line in handle:
    line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.translate(line.maketrans('', '', '1234567890'))
    list0 = line.lower().split()
    for x in list0:
        for y in x:
            dict1[y] = dict1.get(y, 0) + 1

list1 = list()

for k, v in dict1.items():
    list1.append( (v, k) )
    list1.sort(reverse=True)

for k, v in list1:
    print(v, k)