import random

rpc = ["""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""", """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""", """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""]

print("""

┌───────────────────────────────┐
│       ROCK  PAPER  SCISSORS   │
└───────────────────────────────┘

""")

print("Welcome to rock, paper, scissors game!\nFollow the instructions to play the game:\nEnter 0 for ROCK\nEnter 1 for PAPER\nEnter 2 for SCISSORS")


def rpc_game():
    while True:
        index = random.randint(0, 2)
        user_choice = input('Make a choice!\n:').strip()

        if not user_choice.isdigit() or not (0 <= int(user_choice) <= 2):
            print('Please pick 0, 1 or 2.')
            continue
         
        user_choice = int(user_choice)

        if user_choice == index:
            print(f"Computer choice:\n{rpc[index]}")
            print(f"Your choice:\n{rpc[user_choice]}")
            print('That was a draw!')
            break
        elif (user_choice == 0 and index == 2) or (user_choice == 1 and index == 0) or ( user_choice == 2 and index == 1):
            print(f"Computer choice:\n{rpc[index]}")
            print(f"Your choice:\n{rpc[user_choice]}")
            print('You won!')
            break
        else:
            print(f"Computer choice:\n{rpc[index]}")
            print(f"Your choice:\n{rpc[user_choice]}")
            print('You lost!')
            break
        
while True:
    rpc_game()

    again = input('Do you want to play again(y/n): ').strip().lower()
    while again not in ['y', 'n', 'yes', 'no']:
        again = input('Please type y or n: ')
    
    if again not in ['y', 'yes']:
        break

print('Bye! Thanks for playing!')