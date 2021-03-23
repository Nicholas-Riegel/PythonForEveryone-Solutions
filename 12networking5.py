'''
Exercise 5: (Advanced) Change the socket program so that it only shows data after the headers and a blank line have been received. Remember that recv receives characters (newlines and all), not lines.
'''

import socket
import re

# fullUrl = input('Enter URL: ')
# if len(fullUrl) < 1:
fullUrl = 'http://data.pr4e.org/romeo.txt'
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
    data = mysock.recv(1000)
    if len(data) < 1:
        break
    text += data.decode()

list0 = text.split('\n\r\n')
print(list0[1])

mysock.close()
