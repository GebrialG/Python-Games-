# we will ask the user to make a number of different choices with nested if/else statements
# we can change the options in the statements for example by expanding the number of options or
# store options in variable and use that variable later on
def adventure():
    name = input("Type your name: ")
    print("Welcome", name, "to this adventure")

    answer = input(
    "You are on a dirt road it has come to an end, and you can go left and right, "
    "which way would you like to go, left or right?: ").lower()

    if answer == "left":
        answer = input("You have come to a river, you can walk around it or swim across? Type walk to walk around "
                   "and swim to swim across: ")
        if answer == "swim":
            print("You swam across and were eaten by an alligator")
        elif answer == "walk":
            print("You walked for many miles ran out of water and lost the game")
        else:
            print("Not a valid option. You lose")

    elif answer == "right":
        answer = input("You come to a bridge it looks wobbly do you want to cross it or head back(cross/head back)?: ")

        if answer == "back":
            print("You go back and lose.")
        elif answer == "cross":
            answer = input("You cross the bridge and meet a groups of strangers, do you want to go up and speak to them?: ")

            if answer == "yes":
                print("You talk to the strangers and give you millions of pounds worth of gold, you win!")
            elif answer == "no":
                print("You ignore the strangers and offended they proceed to kill you violently, you lose!")
            else:
                print("Not a valid option, you lose")
        else:
            print("Not a valid option. You lose")
    else:
        print("Not a valid option. You lose")

    print("Thank you for taking part", name)


adventure()
