class Animal:
    def speak(self):
        pass
class Dog(Animal):
    def speak(self):
        return "Woof!"
class Cat(Animal):
    def speak(self):
        return "Meow!"
class kunni(Animal):
    def speak(self):
        return "Chatapata!"
class dummi(Animal):
    def speak(self):
        return "Abadiiii!"
class rojuu(Animal):
    def speak(self):
        return "baleebalee!"
def make_animal_speak(animal):
    print(animal.speak())
dog=Dog()
cat=Cat()
Kunni=kunni()
Dummi=dummi()
Rojuu=rojuu()

make_animal_speak(dog)
make_animal_speak(cat)
make_animal_speak(Kunni)
make_animal_speak(Dummi)
make_animal_speak(Rojuu)