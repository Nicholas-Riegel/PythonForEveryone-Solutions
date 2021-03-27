class PartyAnimal:
    x = 0

    def party(self):
        self.x = self.x + 2
        print('So far', self.x)


yo = PartyAnimal()

yo.party()  # So far 2
yo.party()  # So far 4
yo.party()  # So far 6

print('type', type(yo))
print('dir', dir(yo))