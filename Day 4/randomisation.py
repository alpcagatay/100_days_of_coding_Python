# mersene twister algorithm

import random

# between a and b
random_integer = random.randint(1,10)
print(random_integer)

# Module : different functionality for each
# To create your own module create a file with py 
# then import it  by import name_of_the_file
# then to call a value from there call it by name_of_the_file.name_of_the_value. 

random_number_0_to_1 = random.random()
print(random_number_0_to_1)

# multiply with 10 you would get between 0 and 10
random_number_0_to_1 = random.random()*10
print(random_number_0_to_1)

random_float = random.uniform(1,10)
print(random_float)

head_or_tail = random.randint(1,2)
if head_or_tail == 1:
    print("Head")
else:
    print("Tail")
