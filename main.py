from replit import clear
from art import logo

def find_highest(bidding_record):
  highest_bid = 0
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")

print(logo)
other_bidders = "yes"
bids = {}
while other_bidders == "yes":
  name = input("What is your name?: ")
  price = int(input("What is your bid? $"))
  bids[name] = price
  other_bidders = input("Are there any other bidders? Please type 'yes' or 'no:'")
  if other_bidders == "yes":
    clear()
  elif other_bidders == "no":
    find_highest(bids)