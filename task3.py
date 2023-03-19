class Dog:
    # Class attribute
    species = "Canis familiaris"

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"


miles = Dog("Miles", 4, "Jack Russell Terrier")
buddy = Dog("Buddy", 9, "Dachshund")
jack = Dog("Jack", 3, "Bulldog")
jim = Dog("Jim", 5, "Bulldog")
print()
for dog in (miles, buddy, jack, jim):
    print(dog.name, dog.age, dog.breed)
print()
buddy = buddy.speak("Yap")
jim = jim.speak('Woof')
jack = jack.speak('Woof')

for dog in (buddy, jim, jack):
    print(dog)
