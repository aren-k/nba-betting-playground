from bet_earnings_calc import bet_earnings_calc
import os
import json
import math

# importing all data
cur_path = os.path.dirname(__file__)
f = open(cur_path + "\\raw-data\\22-23-season\\combined-filtered.json")  # open raw data file
all_data = json.load(f)

#set up some variables for final answers
bet_amount = 10
sum = 0
total_wins = 0
total_losses = 0
total_bet_amount = 0

# do the math for every game
for i in range(len(all_data["rows"])):
    sum -= bet_amount
    total_bet_amount += bet_amount
    earnings = bet_earnings_calc(bet_amount, all_data["rows"][i])
    if earnings > 0:
        total_wins += 1
    else:
        total_losses += 1
    sum += earnings

# print our data
print("total winnings (losses) is: $" + str(math.floor(sum)))
print("total won bets is: " + str(total_wins))
print("total lost bets is: " + str(total_losses))
print("total bet amount is: $" + str(-total_bet_amount))
