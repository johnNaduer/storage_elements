class Animal:
    pass

class Dog(Animal):
    pass

dog = Dog()

print(isinstance(dog, Dog)) # True
print(isinstance(dog, Animal)) # True
print(isinstance(dog, int)) # False
