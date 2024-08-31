import random

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i",
           "j", "k", "l", "m", "n", "o", "p", "q", "r",
           "s", "t", "u", "v", "w", "x", "y", "z"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "9", "8", "0"]
symbols = ["!", "@", "#", "$", "%", "¨", "&", "*", "(", ")", "_", "+", "=", "-"]


print("Welcome to the PyPassword Generator!")
length = int(input("How many letters would you like in  your password? "))
symbol = int(input("How many symbols would you like? "))
number = int(input("How many numbers would you like? "))

# easy 

password = []
new_pass = ""

for len in range(0,length):
    password.append(random.choice(letters))

for sym in range(0,symbol):
    password.append(random.choice(symbols))

for sym in range(0,symbol):
    password.append(random.choice(numbers))


random.shuffle(password)
print("".join(password))
