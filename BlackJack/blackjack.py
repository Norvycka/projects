import random
from fart import logo


def deal_card():
    """Returns random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """The parameter ^cards is just a placeholder, not the list cards from the function deal_card"""
    if sum(cards) == 21: #len(2), what if the hand is more than 2?
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    
    return sum(cards)

def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over, you lost."
    elif computer_score == user_score:
        return "Draw."
    elif computer_score == 0:
        return "Computer have won, by blackjack."
    elif user_score == 0:
        return "Player have won by blackjack."
    elif user_score > 21:
        return "You went over, you lost."
    elif computer_score > 21:
        return "Computer went over, you won!"
    elif user_score > computer_score:
        return "Player won by highscore!"
    else:
        return "Computer won by highscore!"

def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
        
    while is_game_over == False:
        
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards} and your score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")
        
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Do you want to draw a card? y n ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
                user_score = calculate_score(user_cards)
            else:
                is_game_over = True
                
        while computer_score != 0 and computer_score < 17:
            computer_cards.append(deal_card())
            computer_score = calculate_score(computer_cards)
            
    """Added this v so the user wouldnt see the 0 from calculate_score function"""      
    if user_score == 0:
        user_score = 21
    if computer_score == 0:
        computer_score = 21
      
    print(f"Your final hand was: {user_cards} and final score: {user_score}")
    print(f"Computers hand was: {computer_cards} and final score: {computer_score}")
    print(compare(user_score, computer_score))
            
    while input("Do you want to play blackjack again? y n ") == "y":
        play_game()
        
play_game()
