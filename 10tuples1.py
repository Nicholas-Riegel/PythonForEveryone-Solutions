'''
Exercise 1: Revise a previous program as follows: Read and parse the "From" lines and pull out the addresses from the line. Count the number of messages from each person using a dictionary. After all the data has been read, print the person with the most commits by creating a list of (count, email) tuples from the dictionary. Then sort the list in reverse order and print out the person who has the most commits. 

Sample Line:
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

Enter a file name: mbox-short.txt
cwen@iupui.edu 5

Enter a file name: mbox.txt
zqian@umich.edu 195  
'''

name = input("Enter file: ")
if len(name) < 1:
    name = "mbox-short.txt"

try:
    handle = open(name)
except:
    print('File not found')
    quit()

dic = dict()

for line in handle:
    if line.startswith('From '):
        list1 = line.split()
        if '@' in list1[1]:
            address = list1[1]
            dic[address] = dic.get(address, 0) + 1

list2 = list()
for k, v in dic.items():
    list2.append((v, k))

k, v = max(list2)
print(v,k)
