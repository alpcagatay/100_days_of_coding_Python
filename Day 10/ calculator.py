def add(n1, n2):
    return n1 + n2

def substract(n1, n2):
    return n1 + n2


def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

functions_dict = {"+":add,
                  "-":substract,
                  "*":multiply,
                  "/":divide}






def calculator():
    to_continue = True
    first_number = float(input("What's the first number?: "))

    while to_continue:
        
        print("+\n-\n*\n/\n")
        operator = str(input("Pick an operation: "))
        second_number = float(input("What's the second number?: "))
        result = functions_dict[operator](first_number, second_number)
        print(result)
        to_cont = input("Would you like to continue 'y' or 'n' ")
        if to_cont.lower() == 'y':
            to_continue = True
            first_number = result
        elif to_cont.lower() == 'n':
            print("\n" * 20)
            to_continue = False
            calculator()

calculator()