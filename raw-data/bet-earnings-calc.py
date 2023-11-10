"""
Calculates the bet earnings (losses) when making a given bet and given game data. 
Bets are always put on the favourites (based on odds).
Earnings are positive and losses are negative
earnings include the bet amount for example:
    if $10 bet on an outcome with $1.10 odds, total earnings are $11.00, NOT just $1.00
Author: Aren James Kerdokian
Date: 
"""

"""
calculates the winnings by betting on the favourites for a single game
@param bet_amount: amount of money bet on the game
@param row_data: the game data from the combined_filtered json file.

return: earnings (losses) from winning (losing) the bet 
"""
def bet_earnings_calc(bet_amount: float, row_data) -> float:
    home_odds = row_data["home_odds"]
    away_odds = row_data["away_odds"]

    # true if betting on home, false otherwise
    home_bet = home_odds <= away_odds

    # earn money if favourites win, otherwise lose money
    if home_bet and row_data["home-winner"] == "win":
        return bet_amount * home_odds
    if not home_bet and row_data["away-winner"] == "win":
        return bet_amount * away_odds
    return -bet_amount

    
