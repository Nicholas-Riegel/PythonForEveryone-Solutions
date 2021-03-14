'''
Exercise 5: This program records the domain name (instead of the address) where the message was sent from instead of who the mail came from (i.e., the whole email address). At the end of the program, print out the contents of your dictionary. 

python schoolcount.py
Enter a file name: mbox-short.txt
{'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7,
'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}

'''
fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'mbox-short.txt'
try:
    fhandle = open(fname)
except:
    print('File not found:', fname)
    quit()

dic = dict()

for line in fhandle:
    if line.startswith('From '):
        list = line.split()
        if '@' in list[1]:
            email = list[1]
            domain = email[email.find('@')+1:]
            dic[domain] = dic.get(domain, 0) + 1

print(dic)
