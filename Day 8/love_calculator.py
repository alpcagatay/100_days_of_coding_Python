
def calculate_love_score(first,second):
    true_list_1 = ['t','r','u','e']
    love_list_2 = ['l','o','v','e']
    name_combined = first.lower() + second.lower()
    number_of_t = 0
    number_of_r = 0
    number_of_u = 0
    number_of_e = 0
    number_of_l = 0
    number_of_o = 0
    number_of_v = 0

    for char in name_combined:
        if char == "t":
            number_of_t +=1
        elif char == "r":
            number_of_r +=1
        elif char == "u":
            number_of_u +=1
        elif char == "e":
            number_of_e +=1
        elif char == "l":
            number_of_l +=1
        elif char == "o":
            number_of_o +=1
        elif char == "v":
            number_of_v +=1
        else:
            continue
    
    true_sum = number_of_t + number_of_r + number_of_u + number_of_e
    love_sum = number_of_l + number_of_o + number_of_v + number_of_e
    
    love_score = str(true_sum) + str(love_sum)
    print(love_score)


    
    
    
    
    
calculate_love_score("Kanye West","Kim Kardashian")
    
    