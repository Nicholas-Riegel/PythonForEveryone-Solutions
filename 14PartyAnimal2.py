class PartyAnimal:
   x = 0
   name = ''

   def __init__(self, y): # fires upon initialization
     self.name = y
     print(self.name, 'constructed')

   def party(self): # fires upon call
     self.x = self.x + 1
     print(self.name, 'party count', self.x)


s = PartyAnimal('Sally') # Sally constructed
j = PartyAnimal('Jim') # Jim constructed

s.party() # Sally party count 1
j.party() # Jim party count 1
s.party() # Sally party count 2


class CricketFan(PartyAnimal):
   points = 0

   def six(self):
      self.points = self.points + 6
      self.party()
      print(self.name, "points", self.points)


s = PartyAnimal("Sally")
s.party()
j = CricketFan("Jim")
j.party()
j.six()
print(dir(j))
