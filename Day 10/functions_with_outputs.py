# functions:

# def my_function():
#     #do this

# def my_function_2(something):
#     #do this with something
#     print(something)

# Functions with outputs

def with_outputs():
    result = 3 * 2
    return result

# title capitalizes the first letters
def format_name(f_name,l_name):
    formatted_l_name =  l_name.title()
    formatted_f_name =  f_name.title()
    print(formatted_f_name +" " + formatted_l_name)
# title capitalizes the first letters
# def format_name(f_name,l_name):
#     formatted_l_name =  l_name.title()
#     formatted_f_name =  f_name.title()

# title capitalizes the first letters
def format_name(f_name,l_name):
    formatted_l_name =  l_name.title()
    formatted_f_name =  f_name.title()
    return f"{formatted_f_name} {formatted_l_name}"



print(format_name("alp","berk"))


# You can call another function inside of a function.
def function_1(text):
    return text + text

def function_2(text):
    return text.title()

output = function_2(function_1("hello"))

print(output)



def addition(n1,n2):
    return n1 + n2

# you can change the name of the function with the following
my_favourite_operation = addition