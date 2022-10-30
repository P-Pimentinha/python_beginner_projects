import random

r = random.randrange(1,15)
print(r)
guesses = 0

while True:
    guesses += 1
    answer = input("Guess a number: ")
    if answer.isdigit():
        answer = int(answer)
    else:
        print("Please type a number next time")

    if answer == r:
        print("you got it")
        break
    else:
        if answer > r:
            print('you are above the number!')
        else:
            print('you are below the number!')
