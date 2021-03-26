'''
Exercise 1: Change either geojson.py or geoxml.py to print out the two-character country code from the retrieved data. Add error checking so your program does not traceback if the country code is not there. Once you have it working, search for “Atlantic Ocean” and make sure it can handle locations that are not in any country.
'''

#I assume they mean the "short_name" in the last member of the "address_components" list

import urllib.request
import urllib.parse
import urllib.error
import json
import ssl

api_key = 42
serviceurl = 'http://py4e-data.dr-chuck.net/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1:
        quit()

    parms = dict()
    parms['address'] = address

    parms['key'] = api_key

    url = serviceurl + urllib.parse.urlencode(parms)

    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()

    js = json.loads(data)
    # print(json.dumps(js, indent=4))
    
    try:
        countryCode = js['results'][0]['address_components'][len(js['results'][0]['address_components']) - 1]['short_name']
        
    except:
        print('Country code not found')
        quit()

    if len(countryCode) == 2:
        print(countryCode)
    else:
        print('Country code not found')
