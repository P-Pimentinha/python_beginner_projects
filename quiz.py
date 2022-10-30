print('Welcome Player!')

switch = True
score = 0

while switch:
    x = input('In the mood for some DragonBall Quiz?(yes/no): ')
    if x == 'yes':
        break
    elif x == 'no':
        quit()
    else:
        continue

print("answer by typing the number that is associated to the answer you want to give")

answer = input("how many different dragon balls are there \n"
               "7 / 8 / 6 / 12 : ")
if answer == "7":
    score += 1
    print("correct")
else:
    print("incorrect")

answer = input("What is Goku's signature attack? \n"
               "1:Go ninjas go! / 2:Dragon Power / 3: Kamehameha / 4:Time to Duel! ")
if answer == "3":
    score += 1
    print("correct")
else:
    print("incorrect")

answer = input("What is the name of Master Roshi's school? \n"
               "1:The Tortoise school / 2:The Dragon School / 3: The Turtle School / 4:St Dunstan´s Academy for Young Ladies ")
if answer == "3":
    score += 1
    print("correct")
else:
    print("incorrect")

print("Your score: " + str(score))




