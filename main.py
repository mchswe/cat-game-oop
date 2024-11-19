from cats import Cat

print("Welcome to my Cat Game!")

given_name = input("What is your Cat's name?")
given_colour = input("What colour is your Cat?")

cat1 = Cat(given_name, given_colour)

play_state = True

while play_state == True:
    option = input("What would you like to do? 1.Play 2.Train. 3.Feed 4.Sleep. 5.View Cat's Stats 6.Exit Game")
    
    if option == "1":
        play()
    elif option == "2":
        train()
    elif option == "3":

    elif option == "4":

    elif option == "5":

    elif option == "6":
        play_state = False
        break
    else:
        pass