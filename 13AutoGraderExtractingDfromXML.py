import urllib.request
import urllib.parse
import urllib.error
import xml.etree.ElementTree as ET
import ssl

# url = input('Enter URL: ')
# if url == '':
    # url = "http://py4e-data.dr-chuck.net/comments_42.xml"
url = "http://py4e-data.dr-chuck.net/comments_1178896.xml"

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

fhandle = urllib.request.urlopen(url, context=ctx)
string = fhandle.read().decode()

xml = ET.fromstring(string)
list0 = xml.findall('comments/comment/count')

list1 = list()

for x in list0:
    list1.append(float(x.text))

print('Count:', len(list1))
print('Sum:', sum(list1))
