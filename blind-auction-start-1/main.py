from replit import clear
from art import logo

#HINT: You can call clear() to clear the output in the console.

print(logo)
bids_dictionary = {}
bids_remaining = True

def add_bid(bid_name, bid_amount):
  bids_dictionary[bid_name] = bid_amount

def find_highest_bid(bids):
  highest_bid = 0
  highest_bidder = ""
  for name in bids:
    if int(bids[name]) > highest_bid:
      highest_bidder = name
      highest_bid = int(bids[name])
  print(f"The highest bid was made by {highest_bidder}, with a bid of ${highest_bid}.")

while bids_remaining:
  name = input("What's your name? ")
  bid = input("What's your bid? $")

  add_bid(bid_name=name, bid_amount=bid)

  bids_left = input("Are there any bids remaining? Please write 'yes' or 'no' ")
  clear()
  if bids_left == 'no':
    bids_remaining = False
clear()
find_highest_bid(bids=bids_dictionary)
