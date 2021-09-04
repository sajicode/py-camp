class Pet:
  allowed = ['cat', 'dog', 'fish', 'porcupine']
  def __init__(self, name, species):
    if species not in Pet.allowed:
      raise ValueError(f"You can't have a {species} pet")
    self.name = name
    self.species = species

# cat = Pet("Pink", "cats")

# print(cat)


class Chicken():
  total_eggs = 0
  def __init__(self, name, species):
    self.name = name
    self.species = species
    self.eggs = 0

  def lay_egg(self):
    self.eggs += 1
    Chicken.total_eggs += 1
    return self.eggs

chic1 = Chicken('Alice', 'Aves')
chic2 = Chicken('Amelia', 'Bird')

chic1.lay_egg()
chic2.lay_egg()

# print(chic1.lay_egg())
# print(Chicken.total_eggs)