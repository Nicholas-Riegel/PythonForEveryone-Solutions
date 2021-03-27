class PartyAnimal:
   x = 0
   name = ''

   def __init__(self, y):  # fires upon initialization
     self.name = y
     print(self.name, 'constructed')

   def party(self):  # fires upon call
     self.x = self.x + 1
     print(self.name, 'party count', self.x)



class CricketFan(PartyAnimal):
   points = 0

   def six(self):
      self.points = self.points + 6
      self.party()
      print(self.name, "points", self.points)


s = PartyAnimal("Sally") # Sally constructed
s.party() # Sally party count 1
j = CricketFan("Jim") # Jim constructed
j.party() # Jim party count 1
j.six()  # Jim party count 2
# Jim points 6
print(dir(j))
