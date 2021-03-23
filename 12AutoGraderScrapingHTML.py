
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
if url == '':
    url = 'https://py4e-data.dr-chuck.net/comments_1178894.html'
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all span tags
spans = 0
numbers = []
tags = soup('span')
for tag in tags:
    spans += 1
    numbers.append(float(tag.contents[0]))
print('Count', spans)
print('Sum', sum(numbers))
