class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

class ChildClass:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def print_animals(self):
        for animal in self.animals:
            print(f"Name: {animal.name}, Age: {animal.age}")

# Child class nima?
# Child class - bu bir klassning o'zgaruvchilariga yoki metodlariga kirish uchun yaratilgan klassdir.

child_class = ChildClass()

dog = Dog("Buldog", 3, "Bulldog")
cat = Cat("Mursik", 2, "Qora")

child_class.add_animal(dog)
child_class.add_animal(cat)

child_class.print_animals()
```

Kodda `Dog` va `Cat` klasslari `Animal` klassidan meros olgan holda, ularning o'ziga xos o'zgaruvchilariga ega. `ChildClass` klassi `Animal` klassining o'zgaruvchilariga kirish uchun yaratilgan.
