
import random
import os
from art import logo

def deal_card():
  # returns a random card from a deck
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return random.choice(cards)

def calculate_score(cards):
  # Take a list of cards & returns the score calculated from the cards
  score = sum(cards)
  
  # Check for Blackjack (if score is 21 with 2 cards: an Ace and a 10-value card)
  if score == 21 and len(cards) == 2:
    return 0
    
  # Check for an Ace (11). If the score is over 21, change Ace value to 1.
  if 11 in cards and score > 21:
    cards.remove(11)
    cards.append(1)
    score = sum(cards)
  return score

def compare(user_score, computer_score):
  # Comapring the user and computer scores
  if user_score > 21 and computer_score > 21:
    return "You went over. You lose 😤"
  
  if user_score == computer_score:
    return "Draw 🙃"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack 😱"
  elif user_score == 0:
    return "Win with a Blackjack 😎"
  elif user_score > 21:
    return "You went over. You lose 😭"
  elif computer_score > 21:
    return "Opponent went over. You win 😁"
  elif user_score > computer_score:
    return "You win 😃"
  else:
    return "You lose 😤"

def play_game():
  print(logo)
    
  user_cards = []
  computer_cards = []
  is_gameover = False
    
  #user and computer have 2 cards each appended them in user_cards & computer_cards.
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
    
  # while loops until game is over
  while is_gameover == False:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your cards: {user_cards} and current score: '{user_score}'")
    print(f"Computer's first card: {computer_cards[0]} \n")
    
    #If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends
    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_gameover = True
    else:
      #if they want to draw another card. If yes, then deal_card() function to add another card to the user_cards. If no, then the game has ended.
      draw_another_card = input("Type 'y' for another card or 'n' to pass \n")
      if draw_another_card == "y":
        user_cards.append(deal_card())
      else:
        is_gameover = True
    
    # While loops until the computer's score is over 16. Where it will draw another car & recalcuate computer_score
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
      
  print(f"Your final cards: {user_cards} and final score: '{user_score}'")
  print(f"Computer's final cards: {computer_cards} and final score: '{computer_score}' \n")
  print(compare(user_score, computer_score))
  
#restart the game. If they answer yes, clear the console and start a new game of blackjack using while loop.
while input("Do you want to play a game of Blackjack? Type 'y' or 'n' \n") == "y":
  os.system('cls')
  play_game()
