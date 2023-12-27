import art
import random
from game_data import data_record
import os

#function that prints data in a formatable form
def print_data(data):
  name = data["name"]
  description = data["description"]
  country = data["country"]
  return f"{name}, a {description} from {country}"
  
#Checking follower count & guess will be equal or not
def follower_count(guess, data_a, data_b):
  if data_a["follower_count"] > data_b["follower_count"]:
    if guess == "A":
      return True
    else:
      return False
  else:
    if guess == "B":
      return True
    else:
      return False

score = 0
game_continue = True
data_b = data_record[random.randint(0, len(data_record) - 1)]
print(art.logo)

#Game will continue until you lose
while game_continue:
  #Generating data for choice A & B. 
  data_a = data_b
  data_b = data_record[random.randint(0, len(data_record) - 1)]
  
  #Checking both shouldnt be equal
  while data_a == data_b:
    data_b = data_record[random.randint(0, len(data_record) - 1)]
  
  print(f"Compare A : {print_data(data_a)}")
  print(art.vs)
  print(f"Against B : {print_data(data_b)}")
  guess = input("\n Who has more followers?\n Type 'A' or 'B': ").upper()
  
  guess_correct = follower_count(guess, data_a, data_b)
  
  if guess_correct:
    os.system('cls')
    score += 1
    print(f"You're right! Your current score is '{score}'")
  else:
    game_continue = False
    print(f"\n You're wrong! Your final score is '{score}'")