#ascii.co.uk/art to get the arts.


# to print ascii art use ''' in the beginning and end

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
*******************************************************************************''')

print("Welcome to Treasure Island")
print("Your mission is to find the treasure")
# use \ before ' or " to make sure that the following char is considered as text"

choice_1 = input("You\'re at a cross road. Where do you want to go?\n\t Type \"left\" or \"right\"").lower()
print(choice_1)


if choice_1 == "left":
    
    
    choice_2 = input("You've come to a lake, there is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across.").lower()
    
    if choice_2 == "wait":
        
        choice_3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. What colour do you pick? ").lower()
        if choice_3 == "red":
            print("It's a room full of fire. Game Over. ")
        elif choice_3 == "yellow":
            print("You found the reasure. You win! ")
        elif choice_3 == "blue":
            print("You enter a room of beasts. Game Over. ")
        else:
            print("You chose a door that doesn't exist. Game Over. ")    
                
    else: 
        print("You got attacked by an angry trout. Game Over. ")
else:
    print("You fell in to a hole. Game Over. ")
