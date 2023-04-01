import time
class Person:
  age = 22
  height = 175.5
  isMale = True
  money = 0
  name = 'Kyryl'

  def __init__(self, name, age):
    self.name = name
    self.age = age


  def work(self, days):
    while days != 0:
      time.sleep(1)
      self.money += 2
      days -= 1

  
  def rest(self, days):
    while days != 0:
      time.sleep(1)
      self.money -= 1
      days -= 1

me = Person('Kyryl', 22)
friend = Person('Vasyl', 20)

print(me.money)
me.work(3)
print("Ви заробили", me.money, "money")


# print(me.age)
# print(friend.age)


# print(me.age)
# friend.name = "Kolya"
# friend.age = 15
# print(friend.name)
