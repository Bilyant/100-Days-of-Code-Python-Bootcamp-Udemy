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
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
direction = input("You're at a crossroad, where do you want to go? Type 'left' or 'right' ").lower()

if direction != "left":
    print("Fall into a hole.Game Over.")
else:
    to_swim_or_not = input("You've come to a lake, there is an island in the middle of the lake. "
                           "Type 'wait' to wait for a boat or type 'seim' to swim across").lower()
    if to_swim_or_not != "swim":
        print("You got attacked by an angry trout.Game Over.")
    else:
        door = input("You arrive at the island unharmed. There is a house with 3 doors."
                     " One red, one yellow and one blue. Which color do you choose?").lower()
        if door == "blue":
            print("You got eaten by beasts.Game Over.")
        elif door == "red":
            print("It's a room full of fire.Game Over.")
        elif door == "yellow":
            print("You found the treasure. You Win!")
        else:
            print("Game Over.")
