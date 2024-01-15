from human import Human
from robot import Robot

class Planet:

  def __init__(self, name):
    self.name = name
    self.inhabitants = []

  def __repr__(self):
    return f"planet(inhabitants={self.inhabitants})"

  def __str__(self):
    return f"This planet has {len(self.inhabitants)} Inhabitants."

  def add(self, inhabitant):
    self.inhabitants.append(inhabitant)

  def remove(self, inhabitant):
    if inhabitant in self.inhabitants:
      self.inhabitants.remove(inhabitant)


if (__name__ == "__main__"):
  planet = Planet("Earth")
  print(repr(planet))
  prins = Human("Prins")
  planet.add(prins)
  print(repr(planet))
  print(planet)