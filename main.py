class Person:
  age = 22
  height = 175.5
  isMale = True
  name = 'Kyryl'

  def __init__(self, name, age):
    self.name = name
    self.age = age

me = Person()
friend = Person()

print(me.age)
friend.name = "Kolya"
friend.age = 15
print(friend.name)
