def greet_with(name,location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

greet_with("Jack","nowhere")

# the order of the arguments matter!

# in this case position does not matter
greet_with(name="Jack",location="nowhere")

