#Step 5
import os
import random
import hangman_art
from hangman_words import word_list

# Randomly choosing a word from the word_list and assign it to a variable called chosen_word & storing its length in word_length
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(hangman_art.logo)

# Empty 'display' list & storing '_' For each letter in the chosen_word
display = []
for _ in range(word_length):
  display += "_"

# While end when all 6 lives are exhausted
while not end_of_game:
  guess = input("Guess a letter: ").lower()
  os.system("clear")

  if guess in display:
    print(f"You've already guessed {guess}")

  #Check guessed letter is one of the chosen_word by its position and add that letter in the same position to 'display' list
  for position in range(word_length):
    letter = chosen_word[position]
    # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
    if letter == guess:
      display[position] = letter

  # They chosen a wrong letter they loses a live. If lives goes down to 0 then the game will stop and 'You lose'
  if guess not in chosen_word:        
    lives -= 1
    print(f"You guessed {guess}, that's not in the word. You have {lives} lives left.")
    if lives == 0:
      end_of_game = True
      print("You lose.")
      print(f"The word was {chosen_word}")

  #Join all the elements in the list and turn it into a String.
  print(f"{' '.join(display)}")

  #Check if user has got all letters.
  if "_" not in display:
    end_of_game = True
    print("You win.")

  #print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
  print(hangman_art.stages[lives])
