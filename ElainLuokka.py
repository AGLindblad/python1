class Animal():
  name = "Geneerinen kaveri"

  def sound(self):
    return "Epämääräistä mölinää"

class Lion (Animal):
  def sound(self):
    return "Roarrrr"

lion = Lion()
print(lion.sound())
