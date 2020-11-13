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
#Imports
# from os import system, name
import random
# from pynput.keyboard import Key, Listener

#Game Logic
# def clear():
  
#     # for windows 
#     if name == 'nt': 
#         _ = system('cls') 
  
#     # for mac and linux(here, os.name is 'posix') 
#     else: 
#         _ = system('clear')

choices = [rock, paper, scissors]
players_choice_as_int = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors "))
players_choice = choices[players_choice_as_int]
print("\n")
print("You chose:")
print(players_choice)
print("\n")
print("Computer chose:")
random_computer_choice = random.randint(0, 2)
computers_choice = choices[random_computer_choice]
print(computers_choice)
print("\n")

if players_choice == computers_choice:
  print("It's a draw.")

elif (players_choice == rock) and (computers_choice == scissors):
  print("You win!")

elif (players_choice == scissors) and (computers_choice == paper):
  print("You win!")

elif (players_choice == paper) and (computers_choice == rock):
  print("You win!")

else:
  print("You lose.")

