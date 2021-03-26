import urllib.request
import urllib.parse
import urllib.error
import json
import ssl

# url = input('Enter URL: ')
# if url == '':
# url = "http://py4e-data.dr-chuck.net/comments_42.json"
url = "http://py4e-data.dr-chuck.net/comments_1178897.json"

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

fhandle = urllib.request.urlopen(url, context=ctx)
string = fhandle.read().decode()

list0 = list()

dict0 = json.loads(string)
for x in dict0['comments']:
    list0.append(float(x['count']))

print('Count:', len(list0))
print('Sum:', sum(list0))
