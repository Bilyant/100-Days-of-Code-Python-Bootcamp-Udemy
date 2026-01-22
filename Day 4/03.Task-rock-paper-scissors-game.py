import random

rock = (
    """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

paper = (
    """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
)

scissors = (
    """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
)

choices = [rock, paper, scissors]

player_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: ")
computer_choice = random.randint(0, 2)

if player_choice not in ["0", "1", "2"]:
    print("Please enter a valid choice.")
    exit()

player_choice = int(player_choice)
print(choices[player_choice])
print("Computer chose:")
print(choices[computer_choice])

if player_choice == computer_choice:
    print("It's a draw")
elif player_choice == 0:
    if computer_choice == 1:
        print("You lose")
    elif computer_choice == 2:
        print("You win")
elif player_choice == 1:
    if computer_choice == 2:
        print("You lose")
    elif computer_choice == 0:
        print("You win")
elif player_choice == 2:
    if computer_choice == 0:
        print("You lose")
    elif computer_choice == 1:
        print("You win")
