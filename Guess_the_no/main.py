import random
import art

print(art.logo)
print("Welcome to the Number Guessing Game!")
print("Think of a number between 1 and 100. \n")

# generating random no & storing it in variable
answer = random.randint(1, 100)

def game(turns):
   
    guess = 0
    # While loop to check that turns greater than 0 & guess not equal to answer & gives its too high or too low
    while turns > 0 and guess != answer:
        print(f"\nYou have {turns} guesses to guess the number.")
        guess = int(input("Make a guess : "))
        if guess > answer:
            print("Too high")
            print(art.try_again)
        elif guess < answer:
            print("Too low.")
            print(art.try_again)
        turns -= 1

    #Exits & checks if guess is equal to answer or not
    if guess == answer:
        print(f"\nYou won! The number was {answer}.")
        print(art.winner)
    else:
        print(f"\nYou lost! The number was {answer}.")
        print(art.lose)

# Sets difficulty and calls game function and passes turns as input
def start_game():
    level = input("Choose a difficulty. Type 'easy' or 'hard':\n")
    if level == 'easy':
        turns = 10
        game(turns)
    elif level == 'hard':
        turns = 5
        game(turns)
    else:
        print("Invalid input. Please choose 'easy' or 'hard'.")
        start_game()

start_game()
