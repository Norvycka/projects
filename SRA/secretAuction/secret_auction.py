from art import logo

print(logo)

bidders = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
  highest_bid = 0
  
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"Winner is a {winner} with a bid ${highest_bid}")

while not bidding_finished:
  name = input("What is your name? ")
  bid = int(input("What is your bid price? "))
  bidders[name] = bid
  should_continue = input("are there any more bidders? Type 'yes' or 'no'.")
  if should_continue == 'no':
    bidding_finished = True
    find_highest_bidder(bidders)
  elif should_continue == 'yes':
    print ("\n" * 100)
