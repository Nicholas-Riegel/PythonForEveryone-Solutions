'''
9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
'''
try: 
    name = input("Enter file: ")
    if len(name) < 1:
        name = "mbox-short.txt"
    handle = open(name)
except:
    print('Error: File not found.')
    quit()

dict = dict()

for x in handle:
    if x.startswith('From '):
        list = x.split()
        email = list[1]
        dict[email] = dict.get(email, 0) + 1

maxval = max(dict.values())

for a, b in dict.items():
    if b == maxval:
        print(a, b)