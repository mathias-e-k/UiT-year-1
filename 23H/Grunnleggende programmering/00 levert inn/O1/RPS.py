from random import randint
player_number = int(input("Rock(0) Paper(1) Scissor(2)! Enter a number from from 0 to 2: "))
while player_number not in [0, 1, 2]:
    print("Your number is not valid")
    player_number = int(input("Rock(0) Paper(1) Scissor(2)! Enter a number from from 0 to 2: "))
computer_number = int(randint(0,2))
shapes = ['Rock', 'Paper', 'Scissor']

if player_number == computer_number:
    print(f"You picked {shapes[player_number]}. Computer picked {shapes[computer_number]}. It's a tie!")
elif player_number == 0 and computer_number == 2 or player_number == 1 and computer_number == 0 or player_number == 2 and computer_number == 1:
    print(f"You picked {shapes[player_number]}. Computer picked {shapes[computer_number]}. You won!")
else:
    print(f"You picked {shapes[player_number]}. Computer picked {shapes[computer_number]}. You lost!")
