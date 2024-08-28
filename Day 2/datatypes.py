print(len("Hello"))

# Data Types
# Strings - used with ""
# substring starts from 0

# haydi deneyelim cevabı biliyorsan mik aç please

# ilk karakteri basma
print("Hello"[0])
# son karakteri basma
print("Hello"[4])
# başlangıçtan şu indexe kadar
print("Hello"[:3])
# şu indexten sona kadar
print("Hello"[3:])
# tersten sayar
print("Hello"[-1])

# concatenate both
print("123"+"345")

# Integer = wholenumber
# _ is used to see the number easily. it does not affect
print(123+345)

print(123_456_789)

# Floar = there is a decimal point

print(3.1415)

# Boolean = True / False

# len function does not accept int
len("12345")

#Each function works with particular data type
# gives the type of the variable
print(type("Hello"))
print(type(123))
print(type(19.19))
print(type(True))

# Type Conversion/ Casting

#convert to int
int("123")
float()
str()
bool()

print(int("123")+int("456"))

#Value Error

print(int("123")+int("456"))

#Option 1
print("Number of letters in your name: " , len(input("Enter your name")))

# Option 2
print("Number of letters in your name: " , str(len(input("Enter your name"))))
