"""
Polymorphie (falls objektorientiert)
a. Erstelle eine Klassenhierarchie (z. B. „Tier“, „Hund“, „Katze“) und implementiere
überschreibbare Methoden
"""

# Base Class / Super Class / Parent Class / Ancestor
class Animal:
    def make_noise(self):
        print("Ein Geräusch")

# Subclass / Child Class / Derived Class / Descendant
class Dog(Animal):
    def make_noise(self):
        print("Wuff wuff!")

# Subclass / Child Class / Derived Class / Descendant
class Cat(Animal):
    def make_noise(self):
        print( "Miau miau!")


bello = Dog()
kitty = Cat()
foxy = Animal()
animals =[foxy, bello, kitty]

for animal in animals:
    animal.make_noise()