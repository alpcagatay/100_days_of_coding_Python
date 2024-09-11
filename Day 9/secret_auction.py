def find_highest_bidder(bid_dict):

    max_bid = 0
    max_bid_name = ""

    max(bid_dict)
    for bid in bids:
        if bids[bid] > max_bid:
            max_bid = bids[bid]
            max_bid_name = bid
    print(f"The winner is {max_bid_name} with a bid of ${max_bid}")


print("Welcome to the game!")

are_there_others = True

bids = {}


while are_there_others:
    name = str(input("What is your name?: "))
    bid = int(input("What's your bid? $"))
    
    bids[name]=bid
        
    should_continue = input("Are there any other bidders? Type 'yes' or 'no' \n").lower()
    if should_continue == "no":
        are_there_others = False
        find_highest_bidder(bids)
    elif should_continue == "yes":
        print("\n"*20)



