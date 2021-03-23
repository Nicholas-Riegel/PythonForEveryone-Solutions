'''
Exercise 2: Change your socket program so that it counts the number of characters it has received and stops displaying any text after it has shown 3000 characters. The program should retrieve the entire document and count the total number of characters and display the count of the number of characters at the end of the document.
'''

import socket

# fullUrl = input('Enter URL: ')
# if fullUrl == '':
fullUrl = 'http://data.pr4e.org/romeo-full.txt'
host = fullUrl.split('/')[2]

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    mysock.connect((host, 80))
except:
    print('Connection failed. Check URL.')
    quit()
cmd = 'GET '+fullUrl+' HTTP/1.0\r\n\r\n'
cmd = cmd.encode()
mysock.send(cmd)

text = ''

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    text += data.decode()

print(text[:3000])

print('\nThe number of characters is:', len(text))

mysock.close()
