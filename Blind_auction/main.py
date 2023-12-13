import os
from art import logo
print(logo)

bidding_record = {}
# stores all the bids in a dictionary item as bidding record {"a":12, "b":14}
auction_open = True


def find_highest_bidder(bidding_record):
  highest_bid = 0
  for bidder in bidding_record:
    #bidder = a and bid = {"a":12}
    bid_amount = bidding_record[bidder]
    # 12 = {"a":12}[a]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      highest_bidder = bidder
  print(f"The winner is {highest_bidder} with a bid of ₹{highest_bid}")

while auction_open:
  name = input("What is your name? \n")
  print("\n What is your bid price?")
  price = int(input("₹"))
  # we entered bid into empty dictinory {}[a] = 12
  bidding_record[name] = price
  should_continue = input("\n Are they any other bidders? \n Enter 'yes' or 'no' \n").lower()
  if should_continue == "yes":
    os.system("clear")
  elif should_continue == "no":
    auction_open = False
    # changing auction_open to true to break while loop
    find_highest_bidder(bidding_record)
    # calling find_highest_bidder
  else:
    print("\n\n\n Please enter a valid answer")
    break