# if else statement
# if condition:
# do this
# else:
# do this

water_level = 50
if water_level > 80:
    print("Drain water")
else:
    print("Continue")

# replace ticket box project
# indentation is important for us. 

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))


if height >= 120:
    print("You can ride the rollercoaster ")
else:
    print("Sorry you have to grow taller before you can ride. ")

#Comparison Operators:
# >     --> Greater than
# <     --> Less than
# >=    --> Greater than or equal to
# <=    --> Less than or equal to
# ==    --> Equal to
# !=    --> Not equal to
# %     --> gives you the remainder


# odd or even project

number = int(input("What is the number you want to check?"))

if number % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")


# Nested if / else
# if condition:
#     if another condition:
#         do this
#     else:
#         do this
# else:
#     do this

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))


if height >= 120:
    print("You can ride the rollercoaster ")
    age = int(input("What is your age? "))
    if age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Sorry you have to grow taller before you can ride. ")

# Nested if with elif
# if condition:
#     do this
# elif:
#     do that
# else:
#     do that


print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))


if height >= 120:
    print("You can ride the rollercoaster ")
    age = int(input("What is your age? "))
    if age <= 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Sorry you have to grow taller before you can ride. ")

#bmi example

weight = 85
height = 1.85

bmi = weight / (height ** 2)

if bmi < 18.5:
    print("underweight")
elif bmi <25:
    print("normal weight")
else:
    print(overweight)

# checking multiple collection


print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))


if height >= 120:
    print("You can ride the rollercoaster ")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
    elif age <= 18:
        bill = 7
    else:
        bill = 12
    
    wants_photo = input("Do you want to have a photo take? Type y for Yes and n for No. ")
    if wants_photo == "y":
        # add $3 to their bill
        bill += 3
    print(f"Your final bill is {bill}")
else:
    print("Sorry you have to grow taller before you can ride. ")
