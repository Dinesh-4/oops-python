class Dog:
    def speak(self):
        return "Woof!"
    
class Cat:
    def speak(self):
        return "Meow!"
    
#with Polymorphism
def animal_speak(animal):
    return animal.speak()

dog = Dog()
cat = Cat()

# print(dog.speak())
print(animal_speak(dog))
print(animal_speak(cat))

#--------------------------------------------


class Dog:
    def speak(self):
        return "Woof!"
    
class Cat:
    def speak(self):
        return "Meow!"
    
#without Polymorphism
def animal_speak(animal):
    if isinstance(animal, Dog):
        return animal.speak()
    elif isinstance(animal, Cat):
        return animal.speak()
        


dog = Dog()
cat = Cat()

# print(dog.speak())
print(animal_speak(dog))
print(animal_speak(cat))












    
