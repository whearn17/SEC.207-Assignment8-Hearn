# Will Hearn
# Python Programing
# Assignment 8


class Bird:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def introduce(self):
        print("Hi my name is " + self.name + " and I am a " + self.species)

    def change_species(self, species):
        self.species = species


if __name__ == '__main__':
    bird1 = Bird(input("Enter name of bird --> "), input("Enter species of bird --> "))
    bird2 = Bird(input("Enter name of bird --> "), input("Enter species of bird --> "))
    bird1.introduce()
    bird2.introduce()
    bird1.change_species(input("Enter a new species for the first bird --> "))
    bird1.introduce()
    method_list = [method for method in dir(Bird) if method.startswith('__') is False]
    print("Attributes --> ", bird1.__dict__, "\nMethods --> ", method_list)
    print()
    print("Attributes --> ", bird2.__dict__, "\nMethods --> ", method_list)


