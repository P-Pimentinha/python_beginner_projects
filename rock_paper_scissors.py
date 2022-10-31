import random


pc_choices = ["rock", 'paper', 'scissors']


while True:

    r = random.randrange(0, 3)
    ai = pc_choices[r]
    print(ai)
    player = input("Play: rock, paper, scissor: ").lower()

    if player not in pc_choices:
        print("Try again")
        continue

    if player == ai:
        print('that was a Draw. Try again')
        continue

    if player == "rock" and ai == 'scissors':
        print('you win')
        break

    if player == "scissors" and ai == 'paper':
        print('you win')
        break

    if player == "paper" and ai == 'rock':
        print('you win')
        break

    print(ai)
    print("You lose")
    print("-------------------------------------")