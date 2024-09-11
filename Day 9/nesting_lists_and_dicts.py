# Nesting : putting 1 inside the other.
# List embedded in dictionary

capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

# nested list in dictionary

travel_log = {
    "France" : ["Paris","Lille","Dijon"],
    "Germany": ["Stuttgart","Berlin"]
}

# to call Lille
print(travel_log["France"][1])

nested_list = ["A","B",["C","D"]]

# to print D
print(nested_list[2][1])


travel_log_with_dic = {
    "France" : {
        "cities_visited":["Paris","Lille","Dijon"],
        "total_visits":12   
    } 
    ,
    "Germany": {
        "cities_visited":["Berlin","Hamburg","Stuttgart"],
        "total_visits":5
        }
}

# to print stuttgart

print(travel_log_with_dic["Germany"]["cities_visited"][2])