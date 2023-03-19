class Dog:
    """
    super() does much more than just search the parent class for a method or an attribute. It traverses the entire
    class hierarchy for a matching method or attribute. If you aren’t careful, super() can have surprising results.
    """
    # Class attribute
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} barks: {sound}"


class JackRussellTerrier(Dog):
    def speak(self, sound="Arf"):
        # return f"{self.name} says {sound}"

        # You can access the parent class from inside a method of a child class by using super():
        return super().speak(sound)


class Dachshund(Dog):
    def speak(self, sound="Arf"):
        return f"{self.name} says {sound}"


class Bulldog(Dog):
    pass


# Instance
miles = JackRussellTerrier("Miles", 4)
buddy = Dachshund("Buddy", 9)
jack = Bulldog("Jack", 3)
jim = Bulldog("Jim", 5)
# Loop through instance
for dog in (miles, buddy, jack, jim):
    print(dog.name, dog.age)
print()
print(miles.species)
print(buddy.name)
print(jack)
print(jack.speak("Woof"))
# To determine which class a given object belongs to, you can use the built-in type():
print(type(miles))
print(type(buddy))
print(type(jack))
print(type(jim))
# Determine if miles is also an instance of the Dog class
print(isinstance(miles, Dog))
print(isinstance(miles, Bulldog))
print(isinstance(jack, Dachshund))

# Extending the functionality of a parent class
miles = JackRussellTerrier("Miles", 4)
print(miles.speak())
print(miles.speak("Grrr"))

# Changes to the parent class automatically propagate to child classes
jim = Bulldog("Jim", 5)
print(jim.speak("Woof"))

# However, calling .speak() on a JackRussellTerrier instance won’t show the new style of output:
miles = JackRussellTerrier("Miles", 4)
print(miles.speak())

# Without super()
buddy = Dachshund("Buddy", 9)
print(buddy.speak())
