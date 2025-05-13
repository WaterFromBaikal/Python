# empty class
from platform import machine


class A1:
    pass
# class with empty params
class A2:
    name = ''
    age = ''

class Cat:
    __slots__ = ['name', 'age']
    def __init__(self, name, age):
        self.name = name
        self.age = age

cat1 = Cat('', '')
cat1.age = 5
cat1.name = 'Whiskers'
# cat1.color = 'red'

# print(cat1.name, cat1.color)
class Dog:
    def __init__(self, name, age):
        if not isinstance(age, int):
            raise TypeError("age должно быть целым числом")
        self.name = name
        self.age = age
    def bark(self):
        print("Woof!")
    def birthday(self):
        self.age+=1
    def isPuppy(self):
        if self.age < 2:
            return True
        else: return False

dog1 = Dog('Bob',1)
dog1.bark()
print(dog1.age)
dog1.birthday()
print(f'У собаки {dog1.name} сегодя день рождения! Ей исполнилось {dog1.age} лет')
dog2 = Dog('Elsa', 1)
print(dog1.isPuppy())
print(dog2.isPuppy())
dog3 = Dog('Eve', 7)
dogs_list = [dog1, dog2, dog3]
print(max([i.age for i in dogs_list]))

def getAge(Dog):
    return Dog.age

print(max(dogs_list, key = getAge).name)