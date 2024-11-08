class Cat: # cat entity
    # Constructor - creates cat in the code, to create cat - needs given_name & given_colour
    def __init__(self, given_name, given_colour):
        self.name = given_name
        self.colour = given_colour
        self.age = 1
        self.energy = 50
        self.intelligence = 10
        self.weight = 5

    def train(self):
        print(f"{self.name} is training...")
        self.intelligence += 1
        self.energy -= 5
        self.age += 0.2

    def feed(self):
        print (f"{self.name} is eating...")
        self.energy += 5
        self.weight += 1
        self.age += 0.2

    def play(self):
        print(f"{self.name} is playing...")
        self.energy -= 2
        self.weight -= 1
        self.age += 0.2

    def sleep(self):
        print(f"{self.name} is sleeping...")
        self.energy += 5
        self.age += 0.2

    def view_stats(self):
        print(f"{self.name} is {self.age} years old. \n Colour: {self.colour} \n Intelligence: {self.intelligence} \n Energy: {self.energy} \n Weight: {self.weight} ")

    
