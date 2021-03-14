'''
Exercise 3: Write a program to read through a mail log, build a histogram using a dictionary to count how many messages have come from each email address, and print the dictionary. 

Enter file name: mbox-short.txt
{'gopal.ramasammycook@gmail.com': 1, 'louis@media.berkeley.edu': 3,
'cwen@iupui.edu': 5, 'antranig@caret.cam.ac.uk': 1,
'rjlowe@iupui.edu': 2, 'gsilver@umich.edu': 3,
'david.horwitz@uct.ac.za': 4, 'wagnermr@iupui.edu': 1,
'zqian@umich.edu': 4, 'stephen.marquard@uct.ac.za': 2,
'ray@media.berkeley.edu': 1}

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
            dic[email] = dic.get(email, 0) + 1

print(dic)
