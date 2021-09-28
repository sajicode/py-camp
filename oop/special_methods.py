class Human:
  """Human class

    Args:
      first(string): first name
      last(string): last name
      age(int):  the age

  """
  def __init__(self, first, last, age):
    self.first = first
    self.last = last
    self.age =  age

  def __repr__(self):
    return f"Human named {self.first} {self.last}"

  def __len__(self):
    return self.age

#* magic methods below
  def __add__(self, other):
    if isinstance(other, Human):
      return Human(first="Newborn", last=self.last, age=0)
    return "You can't add that!"

q = Human("Cleopatra", "Rameses", 42)

print(q + 2)