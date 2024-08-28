print("----Treasure Island----")

choice1 = input("You are at the crossroad.Where do you want to go?Type left or right").lower()
if choice1 == "left":
    choice2 = input("You come to a Lake.There is an island in the middle of the lake.Type 'wait' for waiting and 'swim' for swimming across ")
    if choice2 == "wait":
        choice3 = input("you arrived at the island unharmed.There is a house with 3 doors.One red,One yeelow and one blue.Choose one")
        if choice3 == "red":
            print("Its a room full of fire,Game over!!")
        elif choice3 == "yellow":
            print("You found the treasure!!!")
        elif choice3 == "blue":
            print("you entered a room full of beasts.Game over!!!")
        else:
            print("YOu chose the door that doesn't exist.Game Over! ")
    else:
        print("You are attacked by an angry trout.Game over")

else:
    print("You chose the wrong way.Fell into the hole.Game over!")