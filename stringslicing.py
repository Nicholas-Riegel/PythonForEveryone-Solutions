data = "from stephen.marquard@uct.ac.za Sat"
posat = data.find('@')
possp = data.find(' ', posat)
host = data[ posat+1 : possp ]

print(host)