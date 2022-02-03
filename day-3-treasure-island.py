print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
crossroad = input(
    "You're at a crossroad. Where do you want to go? Type 'left' or 'right'. ").lower()
if crossroad == "left":
    fight_pirate = input(
        "You encounter a pirate. Do you want to fight or flee? Type 'fight' or 'flee'. ").lower()
    if fight_pirate == "fight":
        print("You got shot in the belly, you fool. Game Over!")
    else:
        print("Run you Forrest! Run!")
        house = input(
            "You discover an abandoned house. Do you want to enter? Type 'Y' for yes or 'N' for no. ").lower()
        if house == "y":
            door = input("You stand in front of three doors. Which one do you want to open? Type 'R' for the red one, 'G' for the green one, 'B' for the black one, or 'N' to do nothing. ").lower()
            if door == 'r':
                print(
                    "You open the red door and get chocked by a thousand strawberries. Game Over!")
            elif door == 'g':
                print(
                    "You open the green door and get smacked by a thousand watermelons. Game Over!")
            elif door == 'b':
                print(
                    "You enter a dark room with a treasure in the center. You open the chest and find nothing...")
            else:
                print("The house exploded. Over Over!")
        else:
            print("You got strangled by wet noodles. Game over.")
else:
    print("You got eaten by a tomato. Game Over!")
