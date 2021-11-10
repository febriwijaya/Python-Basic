class Dog():
  species = "Canis familiriasi"

  def __init__(self, name, age):
    self.name = name
    self.age = age

miles = Dog('Miles', 4)
print(miles.name)
print(miles.age)
print(miles.species)

buddy = Dog('Buddy', 9)
print(buddy.species)