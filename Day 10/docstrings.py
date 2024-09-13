# Docstrings are a way to create little bits of documentation as we're coding alond. 

def format_name(f_name,l_name):
    """Interpreted area"""
    print(f_name + l_name)

format_name("a","b")


def outer_function(a, b):
    def inner_function(c, d):
        return c + d
    return inner_function(a, b)
 
result = outer_function(5, 10)
print(result)




