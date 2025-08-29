# Implement a program that demonstrates polymorphism
#  by creating a base class and derived classes with overridden
#  methods.

class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

if __name__ == "__main__":
    animals = [Dog(), Cat(), Animal()]
    for animal in animals:
        animal.speak()