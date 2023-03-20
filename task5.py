class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return F"{self.name} is {self.age} years old"

    def speak(self, sound):  # sef speak(self, argument)
        return F"{self.name} says {sound}"


class GoldenRetriever(Dog):
    def speak(self, sound="Bark"):
        return f"{self.name} says {sound}"

class BostonTerriers(Dog):
    def speak(self, sound="Yap"):
        return super().speak(sound)


print(GoldenRetriever("Gogo", 5).speak())
print(BostonTerriers("Mil", 3).speak())
