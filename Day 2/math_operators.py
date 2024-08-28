# + addition
# * multiplication
# - substraction
# / division
# ** to the power
# // --> removes the decimals from the result. 6 //4 = 1

# PEMDAS
# ()
# **
# * OR /
# + OR - 

print(3*3+3/3-3)

print(3*(3+3)/3-3)


bmi = 84 / 1.65 ** 2

print(bmi)
#rounds down only
print(int(bmi))
#rounds the number
print(round(bmi))
#rounds the number with n decimals
print(round(bmi,2))

# score = score + 1 = score += 1

#f-strings
score = 0
height = 1.8
is_winning = True

print(f"Your score is = {score}, your height is {height}. You are winning is {is_winning}")
