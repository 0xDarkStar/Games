from tkinter import *
import mine_logic

colors = {0:"white", 1:"blue", 2:"green", 3:"red", 4:"purple", 5:"red4", 6:"cyan3", 7:"black", 8:"gray"}

def null(): # no purpose
   pass

def reveal_self(gameboard, gameboardState, x, y, button, gameFrame = 0, gameboardButtons = 0, minePositions = []):
    gameboardState[y][x] = "S" # Is now Seen
    if gameboard[y][x] == "💣": # It was a bomb
        button.configure(text=gameboard[y][x], bg="red")
        for i in minePositions:
            gameboardButtons[i[0]][str(i[1])].configure(text="💣")
        for i in range(len(gameboardButtons)):
            for ii in list(gameboardButtons[i].keys()):
                gameboardButtons[i][ii].configure(state="disabled")
    elif gameboard[y][x] == "C": # It was the first click
        gameboard[y][x] = "S" # This is the start
        minePositions = mine_logic.add_mines(gameboard)
        mine_logic.add_nearby_mines_number(gameboard)
        makeButtons(gameboard, gameFrame, gameboardButtons, gameboardState, minePositions) # Remake the buttons to have the proper functions
        if gameboard[y][x] == 0: # It was an empty space
            find_adjacent_empty_spaces(gameboard, gameboardState, x, y, button, gameboardButtons)
        else: # It had a number
            button.configure(text=gameboard[y][x], font=("Arial 12 bold"), fg=colors[gameboard[y][x]], bg="white", command=null)
    else: # New space found
        button.configure(text=gameboard[y][x], font=("Arial 12 bold"), fg=colors[gameboard[y][x]], bg="white", command=null)

def find_adjacent_empty_spaces(gameboard, gameboardState, x, y, button, gameboardButtons):
    reveal_self(gameboard, gameboardState, x, y, button)
    area = find_adjacent_area(x, y) # Find the area to search
    for i in area:
        for ii in i: # Seach that entire area
            if ii[0] == 99 or ii[1] == 99: # It was out of bound (skip)
                continue
            elif gameboardState[ii[0]][ii[1]] == "S": # It was seen before (skip)
                continue
            if gameboard[ii[0]][ii[1]] == 0: # It's another zero! (recursion)
                find_adjacent_empty_spaces(gameboard, gameboardState, ii[1], ii[0], gameboardButtons[ii[0]][str(ii[1])], gameboardButtons)
            else: # Number not zero
                reveal_self(gameboard, gameboardState, ii[1], ii[0], gameboardButtons[ii[0]][str(ii[1])])

def find_adjacent_area(x, y):
    coords = [[[0,0], [0,0], [0,0]],
              [[0,0], [0,0], [0,0]],
              [[0,0], [0,0], [0,0]]]
    for i in range(-1,2): # Used to find y coords of surrounding area
        for ii in range(-1,2): # Used to find x coords of surrounding area
            if x+ii >= 0 and x+ii <= 29: # Adding ii doesn't go out of bounds?
                coords[i][ii][1] = x+ii # Add it to the list
            else: # It did go out of bounds
                coords[i][ii][1] = 99 # Report
            if y+i >= 0 and y+i <= 15:
                coords[i][ii][0] = y+i
            else:
                coords[i][ii][0] = 99
    return coords

def makeButtons(gameboard, gameFrame, gameboardButtons, gameboardState, minePositions = []):
    def makeButton(counter, i, ii):
        if gameboard[i][counter] == 0 and gameboardState[i][counter] != "S":
            gameboardButtons[i][ii] = Button(master=gameFrame, text="", width=1, height=1, bg="gray39", command=lambda: find_adjacent_empty_spaces(gameboard, gameboardState, counter, i, gameboardButtons[i][ii], gameboardButtons))
        elif gameboardState[i][counter] != "S":
            gameboardButtons[i][ii] = Button(master=gameFrame, text="", width=1, height=1, bg="gray39", command=lambda: reveal_self(gameboard, gameboardState, counter, i, gameboardButtons[i][ii], gameFrame, gameboardButtons, minePositions))
        gameboardButtons[i][ii].bind("<Button-1>", left_click)
        gameboardButtons[i][ii].bind("<Button-3>", right_click)
        gameboardButtons[i][ii].grid(row=i, column=counter)

    for i in range(len(gameboardButtons)):
        counter = 0
        for ii in list(gameboardButtons[i].keys()):
            makeButton(counter, i, ii)
            counter += 1

def left_click(event):
    if event.widget["state"] == "disabled":
        prevBG = event.widget["bg"]
        event.widget.configure(bg="seagreen1")
        event.widget.after(1000, lambda:event.widget.configure(bg=prevBG))

def right_click(event):
    if event.widget["text"] == "⛳":
        event.widget.configure(text="", bg="gray39")
        event.widget.configure(state="normal")
    elif event.widget["text"] in list(colors.keys()):
        pass
    else:
        event.widget.configure(text="⛳", bg="seashell3")
        event.widget.configure(state="disabled")