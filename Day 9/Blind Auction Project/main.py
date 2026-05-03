# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}

import art
print(art.logo)

def highest_Bidder(bids):
    winner = ""
    highest = 0

    for bidder in bids:
        bid_amount = bids[bidder]

        if bid_amount > highest:
            highest = bid_amount
            winner = bidder

    print(f"The winner is {winner}, with a bid of {highest}!")

# TODO-3: Whether if new bids need to be added
bids = {}
moreBids = True

while moreBids:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price

    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()

    if should_continue == "no":
        moreBids = False
        highest_Bidder(bids)
    elif should_continue == "yes":
        print("\n" * 20)

# TODO-4: Compare bids in dictionary
