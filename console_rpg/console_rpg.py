import playerMovement
import find_guinea_pig as fg
import find_home as fh
import random

# generates the random position of the guinea pig
r1 = random.randrange(1,18)
r2 = random.randrange(19,45)
r3 = [r1, r2]
r4 = random.randrange(0,2)
gp_position = r3[r4]
#print("gp position: " + str(gp_position))

# map of the locations in the grid 4*11
forest = [1, 2, 3, 4, 5, 6, 7, 8]
town = [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
beach = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32]
ocean = [33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44]

home = 18
player = 18
#print("home: " + str(home))
#print("player: " + str(player))

print('Your Guinea Pig just got lost. Bring him Back Home\n'
      'write: up, down, left or right to move around until you find your Guine Pig')

while True:

    #print(player)
    answer = input("Where should we go?: ").lower()

    if answer == 'q':
        quit()

    if answer == 'up':
        if player - 4 < 0:
            print("you reached the limits \n"
                  "-------------------------")
            continue
        else:
            player -= 4
            if fg.findGuineaPig(player, gp_position):
                break
            print(playerMovement.player_Movement(player))
            continue

    if answer == 'down':
        if player + 4 > 44:
            print("you reached the limits \n"
                  "-------------------------")
            continue
        else:
            player += 4
            if fg.findGuineaPig(player, gp_position):
                break
            print(playerMovement.player_Movement(player))
            continue

    if answer == 'left':
        if player - 1 < 0:
            print("you reached the limits \n"
                  "-------------------------")
            continue
        else:
            player -= 1
            if fg.findGuineaPig(player, gp_position):
                break
            print(playerMovement.player_Movement(player))
            continue

    if answer == 'right':
        if player + 1 > 44:
            print("you reached the limits \n"
                  "-------------------------")
            continue
        else:
            player += 1
            if fg.findGuineaPig(player, gp_position):
                break
            print(playerMovement.player_Movement(player))
            continue

print('Your Guinea Pig seems to be starving!! Find your way back home!\n'
      '----------------------------------------------------------\n')

while True:

    print(player)
    answer = input("Where should we go to find home?: ").lower()

    if answer == 'q':
        quit()

    if answer == 'up':
        if player - 4 < 0:
            print("you reached the limits \n"
                  "-------------------------")
            continue
        else:
            player -= 4
            if fh.findHome(player, home):
                break
            print(playerMovement.player_Movement(player))
            continue

    if answer == 'down':
        if player + 4 > 44:
            print("you reached the limits \n"
                  "-------------------------")
            continue
        else:
            player += 4
            if fh.findHome(player, home):
                break
            print(playerMovement.player_Movement(player))
            continue

    if answer == 'left':
        if player - 1 < 0:
            print("you reached the limits \n"
                  "-------------------------")
            continue
        else:
            player -= 1
            if fh.findHome(player, home):
                break
            print(playerMovement.player_Movement(player))
            continue

    if answer == 'right':
        if player + 1 > 44:
            print("you reached the limits \n"
                  "-------------------------")
            continue
        else:
            player += 1
            if fh.findHome(player, home):
                break
            print(playerMovement.player_Movement(player))
            continue

print("The End")