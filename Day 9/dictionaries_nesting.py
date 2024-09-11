# Dictionaries
# key and value

dict_1 = {"bug":"An error in a program","function":"piece of code you keep calling"}

# make sure you wrote the key accurately
print(dict_1["bug"]) # prints the value

# we get key error when we ask for a key that does not exist. 

# adding a new entry
# name_of_the_dict[key_to_be_added] = "vaue to be added"


dict_1["loop"] = "definition of loop"

print(dict_1)

#creating an empty dictionary
empty_dict = {}

# wipe an existing dictionary

# dict1 = {} # this cleans the dictionary


# Edit an item in the dictionary

dict_1["loop"]= "new definition"
print(dict_1)

# loop through dictionary
for thing in dict_1:
    print(thing) # prints the key
    print(dict_1[thing]) # prints the value