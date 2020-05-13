'''
This program allows you to enter as many options as you want, and allows you to enter how many of the options should be randomly chosen.
'''
import random
import sys
moveOn2 = 0
while 1:
    moveOn = 0
    players = []
    while 1:
        player = input("Enter player name, type '/stop' to stop: ")
        if player == "/stop":
            break
        else:
            players.append(player)
    length = int(input("How many people should the program choose? "))
    chosen = []
    for i in range(length):
        moveOn = 0
        while moveOn == 0:
            max = len(players) - 1
            choice = random.randint(0, max)
            if players[choice] in chosen:
                if (len(chosen) == length or len(chosen) == len(players)):
                    break
            else:
                moveOn = 1
        if (len(chosen) == length or len(chosen) == len(players)):
            break
        chosen.append(players[choice])
    print(chosen)
    end = input("Type stop to stop program, enter to continue: ")
    if end == "stop":
        break
sys.exit()
    
    
