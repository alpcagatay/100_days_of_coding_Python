import random

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))

if choice < 0 or choice>2:
    print("Please provide one of the following: 0, 1, 2")


result_list = ["Tie","Win","Lose"]
comp_list = [
'''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)''',
'''     
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)''',
'''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)''']
user_choice = comp_list[choice]
comp_choice = random.choice(comp_list)
result = ""


if choice == 0 :
    user_choice == comp_list[0]
elif choice == 1 :
    user_choice == comp_list[1]
elif choice == 2 :
    user_choice == comp_list[2]
else:
    print("Please provide one of the following: 0,1,2")

if user_choice == "ROCK":
    if comp_choice == "ROCK":
        result = result_list[0]
    elif comp_choice == "SCISSORS":
        result = result_list[1]
    else:
        result = result_list[2]
elif user_choice == "PAPER":
    if comp_choice == "ROCK":
        result = result_list[1]
    elif comp_choice == "SCISSORS":
        result = result_list[2]
    else:
        result = result_list[0]
elif user_choice == "SCISSORS":
    if comp_choice == "ROCK":
        result = result_list[2]
    elif comp_choice == "SCISSORS":
        result = result_list[1]
    else:
        result = result_list[0],
else:
    print("Something's wrong you shouldn't be coming here!")

print(f"You chose {user_choice}")
print(f"Computer chose {comp_choice}")
print(result)
