import urllib.request
import urllib.parse
import urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

api_key = 42
serviceurl = 'http://py4e-data.dr-chuck.net/json?'

address = input('Enter location: ')
if len(address) < 1:
    address = 'Technion'

dict0 = dict()

dict0['address'] = address

dict0['key'] = api_key

url = serviceurl + urllib.parse.urlencode(dict0)

uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()

js = json.loads(data)

id = js['results'][0]['place_id']
print('Place ID:', id)
