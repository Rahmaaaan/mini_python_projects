import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game = [rock, paper, scissors]

#user input & Checking they entered correct input
user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user >= 3 or user < 0:
    print("You typed an invalid number, you lose!")
else:
    print(game[user])

    # generating random number of computer & printing it
    computer = random.randint(0, 2)
    print("Computer choose : ")
    print(game[computer])

    # comparing user & computers choice
    if user == computer:
        print("It is a draw")
    elif user > computer:
        print("You Win")
    elif user < computer:
        print("You lose")
    elif user == 1 and computer == 0:
        print("You win")
    elif user == 0 and computer == 2:
        print("You Win")
    elif user == 2 and computer == 0:
        print("You lose")
    