from cats import Cat

print("Welcome to my Cat Game!")

given_name = input("What is your Cat's name?")
given_colour = input("What colour is your Cat?")

cat1 = Cat(given_name, given_colour)
print(cat1)