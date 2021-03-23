import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter: ')
if url == '':
    url = 'http://py4e-data.dr-chuck.net/known_by_Likitta.html'

times = input('Enter number of times: ')
if times == '':
    times = 7

position = input('Enter position: ')
if position == '':
    position = 18

count = 0

while True:
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    list0 = list()
    anchors = soup('a')
    for x in anchors:
        list0.append(x.get('href', None))
    url = list0[position-1]
    count += 1
    if count == times:
        print(url)
        break
