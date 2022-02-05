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

# Write your code below this line 👇

player_choice = int(
    input("What do you chose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))

options = [rock, paper, scissors]

print(options[player_choice])

computer_choice = random.randint(0, 2)
print("Computer chose: ")
print(options[computer_choice])

if player_choice == computer_choice:
    print("Draw.")
elif player_choice == 0 and computer_choice == 1:
    print("Computer wins")
elif player_choice == 0 and computer_choice == 2:
    print("You win.")
elif player_choice == 1 and computer_choice == 0:
    print("You win.")
elif player_choice == 2 and computer_choice == 0:
    print("Computer wins.")
elif player_choice == 2 and computer_choice == 1:
    print("You win.")
