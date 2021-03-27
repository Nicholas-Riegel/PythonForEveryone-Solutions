class PartyAnimal:
   x = 0

   def __init__(self):  # constructor
     print('I am constructed')

   def party(self):
     self.x = self.x + 1
     print('So far', self.x)

   def __del__(self):  # destructor
     print('I am destructed', self.x)


an = PartyAnimal()  # triggers the constructor
an.party()
an.party()
an = 42  # triggers the destructor
print('an contains', an)
