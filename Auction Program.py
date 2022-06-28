import os
from arti import logo
print(logo)

print("Welcome in Secret Auction Program")

bids = {}
counting_bids = False

def finding_highest_bidder(bidding):
    highest_bid = 0
    winner = ""
    for bidder in bidding:
        bid_amount = bidding[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while not counting_bids:
    name = input("What's your name?")
    price = int(input("What's your bid?: $"))
    bids[name]=price
    decision = input("Are there any other bidders? Type 'yes' or 'no'. \n")
    if decision == "no":
        counting_bids = True
        finding_highest_bidder(bids)
    elif decision == "yes":
        os.system('cls')


