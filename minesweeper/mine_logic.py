import random


def find_offLimits(gameboard):
    for i in range(len(gameboard)):
        for ii in range(len(gameboard[i])):
            if gameboard[i][ii] == "S":
                offLimits = find_adjacent_area(ii, i)
                gameboard[i][ii] = "C"
                return offLimits

def add_mines(gameboard):
    minePositions = []
    offLimits = find_offLimits(gameboard)
    for i in range(len(gameboard)): # Go through entire gameboard
        for ii in range(len(gameboard[i])):
            if [i, ii] in offLimits[0] or [i, ii] in offLimits[1] or [i, ii] in offLimits[2]:
                break
            a = random.random()
            if a >= .8:
                try:
                    gameboard[i][ii] = "💣" # Mine Placed
                    minePositions.append([i, ii])
                except IndexError:
                    break
    return minePositions

def add_nearby_mines_number(gameboard):
    y = 0
    for i in gameboard:
        x = 0
        for ii in i:
            counter = 0 # Count how many mines are nearby
            if ii == "C":
                found_mines = []
                area = find_adjacent_area(x, y) # get array of area to search
                for i2 in area:
                    for ii2 in i2:
                        a = ii2[0]
                        b = ii2[1]
                        if [a, b] not in found_mines:
                            if gameboard[a][b] == "💣": # Mine found!
                                found_mines.append([a, b])
                                counter += 1 # Add to counter
                gameboard[y][x] = counter # Set position to number of mines
            x += 1
        y += 1

def find_adjacent_area(x, y):
    coords = [[[0,0], [0,0], [0,0]],
              [[0,0], [0,0], [0,0]],
              [[0,0], [0,0], [0,0]]]
    for i in range(-1,2):
        for ii in range(-1,2):
            if x+ii >= 0 and x+ii <= 29:
                coords[i][ii][1] = x+ii
            elif x+ii > 29:
                coords[i][ii][1] = 29
            else:
                coords[i][ii][1] = 0
            if y+i >= 0 and y+i <= 15:
                coords[i][ii][0] = y+i
            elif y+i > 15:
                coords[i][ii][0] = 15
            else:
                coords[i][ii][0] = 0
    return coords