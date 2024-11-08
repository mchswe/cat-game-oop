class Cat: # cat entity
    # Constructor - creates cat in the code, to create cat - needs given_name & given_colour
    def __init__(self, given_name, given_colour):
        self.name = given_name
        self.colour = given_colour

# An instance of Cat - Instance: specific occurance of a class
mimi = Cat("Mimi", "Brown")
