name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("left or right, which way you goin dawg? ").lower()

if answer == "left":
    answer = input("around or swim across. Walk or Swim: ")

    if answer == "swim":
        print("You swim across and die dummy.")
    elif answer == "walk":
        print("You died because you dumb bitch.")
    else:
        print("Not a valid option dumb bitch")

elif answer == "right":
    answer = input("Cross or turn back like a bitch? ")

    if answer == "back":
        print("You lose")
    elif answer == "cross":
        answer = input("You cross the dumb bitch bridge and see a foul human. Talk or no? ")
        if answer == "talk":
            print("You Win")
        elif answer == "no":
            print("You died because you dumb bitch.")
        else:
            print("Not a valid option dumb bitch")
    else:
        print("You lose nerd")

else:
    print("not a valid option dumb bitch. you lose")