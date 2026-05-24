print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
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

obstacle1 = input("left or right?")
if obstacle1 == "left" or obstacle1 == "Left":
    print("You turned left and found river!")
    print("You want to cross the river")
    obstacle2 = input("swim or wait?")
    if obstacle2 == "wait" or obstacle2 == "Wait":
        print("You wait for a boat and get to the other side")
        print("You found three doors (red, green, blue)\nChoose one to go inside")
        obstacle3 = input("red or green or blue?")
        if obstacle3 == "green" or obstacle3 == "Green":
            print("You survived and win 67 million dollars")
        elif obstacle3 == "blue" or obstacle3 == "Blue":
            print("You survived. Barely")
        else:
            print("You are dead. Of course.\nGame Over!")
    else:
        print("You drowned\nGame Over!")
else:
    print("You fell into the hole\nGame Over!")