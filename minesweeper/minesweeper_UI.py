from tkinter import *
import reveal_funcs

# A 30x16 gameboard holding where mines are and the number of nearby mines
gameboard = [[[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []],
             [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []],
             [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []],
             [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []],
             [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []],
             [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []],
             [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []],
             [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []],
             [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []],
             [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []],
             [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []],
             [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []],
             [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []],
             [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []],
             [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []],
             [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]]

gameboardButtons = [{"0":0, "1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0, "10":0, "11":0, "12":0, "13":0, "14":0, "15":0, "16":0, "17":0, "18":0, "19":0, "20":0, "21":0, "22":0, "23":0, "24":0, "25":0, "26":0, "27":0, "28":0, "29":0},
                    {"0":0, "1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0, "10":0, "11":0, "12":0, "13":0, "14":0, "15":0, "16":0, "17":0, "18":0, "19":0, "20":0, "21":0, "22":0, "23":0, "24":0, "25":0, "26":0, "27":0, "28":0, "29":0},
                    {"0":0, "1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0, "10":0, "11":0, "12":0, "13":0, "14":0, "15":0, "16":0, "17":0, "18":0, "19":0, "20":0, "21":0, "22":0, "23":0, "24":0, "25":0, "26":0, "27":0, "28":0, "29":0},
                    {"0":0, "1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0, "10":0, "11":0, "12":0, "13":0, "14":0, "15":0, "16":0, "17":0, "18":0, "19":0, "20":0, "21":0, "22":0, "23":0, "24":0, "25":0, "26":0, "27":0, "28":0, "29":0},
                    {"0":0, "1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0, "10":0, "11":0, "12":0, "13":0, "14":0, "15":0, "16":0, "17":0, "18":0, "19":0, "20":0, "21":0, "22":0, "23":0, "24":0, "25":0, "26":0, "27":0, "28":0, "29":0},
                    {"0":0, "1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0, "10":0, "11":0, "12":0, "13":0, "14":0, "15":0, "16":0, "17":0, "18":0, "19":0, "20":0, "21":0, "22":0, "23":0, "24":0, "25":0, "26":0, "27":0, "28":0, "29":0},
                    {"0":0, "1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0, "10":0, "11":0, "12":0, "13":0, "14":0, "15":0, "16":0, "17":0, "18":0, "19":0, "20":0, "21":0, "22":0, "23":0, "24":0, "25":0, "26":0, "27":0, "28":0, "29":0},
                    {"0":0, "1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0, "10":0, "11":0, "12":0, "13":0, "14":0, "15":0, "16":0, "17":0, "18":0, "19":0, "20":0, "21":0, "22":0, "23":0, "24":0, "25":0, "26":0, "27":0, "28":0, "29":0},
                    {"0":0, "1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0, "10":0, "11":0, "12":0, "13":0, "14":0, "15":0, "16":0, "17":0, "18":0, "19":0, "20":0, "21":0, "22":0, "23":0, "24":0, "25":0, "26":0, "27":0, "28":0, "29":0},
                    {"0":0, "1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0, "10":0, "11":0, "12":0, "13":0, "14":0, "15":0, "16":0, "17":0, "18":0, "19":0, "20":0, "21":0, "22":0, "23":0, "24":0, "25":0, "26":0, "27":0, "28":0, "29":0},
                    {"0":0, "1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0, "10":0, "11":0, "12":0, "13":0, "14":0, "15":0, "16":0, "17":0, "18":0, "19":0, "20":0, "21":0, "22":0, "23":0, "24":0, "25":0, "26":0, "27":0, "28":0, "29":0},
                    {"0":0, "1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0, "10":0, "11":0, "12":0, "13":0, "14":0, "15":0, "16":0, "17":0, "18":0, "19":0, "20":0, "21":0, "22":0, "23":0, "24":0, "25":0, "26":0, "27":0, "28":0, "29":0},
                    {"0":0, "1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0, "10":0, "11":0, "12":0, "13":0, "14":0, "15":0, "16":0, "17":0, "18":0, "19":0, "20":0, "21":0, "22":0, "23":0, "24":0, "25":0, "26":0, "27":0, "28":0, "29":0},
                    {"0":0, "1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0, "10":0, "11":0, "12":0, "13":0, "14":0, "15":0, "16":0, "17":0, "18":0, "19":0, "20":0, "21":0, "22":0, "23":0, "24":0, "25":0, "26":0, "27":0, "28":0, "29":0},
                    {"0":0, "1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0, "10":0, "11":0, "12":0, "13":0, "14":0, "15":0, "16":0, "17":0, "18":0, "19":0, "20":0, "21":0, "22":0, "23":0, "24":0, "25":0, "26":0, "27":0, "28":0, "29":0},
                    {"0":0, "1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0, "10":0, "11":0, "12":0, "13":0, "14":0, "15":0, "16":0, "17":0, "18":0, "19":0, "20":0, "21":0, "22":0, "23":0, "24":0, "25":0, "26":0, "27":0, "28":0, "29":0}]

# Holds all the values to know what the player can and can't see, as well as what they've flagged.
gameboardState = [[[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []],
                  [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []],
                  [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []],
                  [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []],
                  [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []],
                  [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []],
                  [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []],
                  [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []],
                  [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []],
                  [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []],
                  [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []],
                  [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []],
                  [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []],
                  [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []],
                  [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []],
                  [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]]

def main():
    global timeLabel, completionLabel
    for i in range(len(gameboard)): # Go through entire gameboard
        for ii in range(len(gameboard[i])):
            gameboard[i][ii] = "C" # Ready to add mines
    for i in range(len(gameboard)): # Go through entire gameboard
        for ii in range(len(gameboard[i])):
            gameboardState[i][ii] = "H" # Hidden
    mainWin = Tk()
    mainWin.geometry("1200x700")
    mainMenu = Menu(mainWin)
    mainMenu.add_command(label="Restart", command=lambda: restart(gameboard, gameboardState, gameFrame))
    statusFrame = Frame(mainWin)
    timeLabel = Label(master=statusFrame, text="00", font="Arial 20 bold")
    timeLabel.pack()
    completionLabel = Label(master=statusFrame, text="You win!")
    gameFrame = Frame(mainWin)
    reveal_funcs.makeButtons(gameboard, gameFrame, gameboardButtons, gameboardState)

    mainWin.config(menu=mainMenu)
    statusFrame.pack()
    gameFrame.pack()
    timeLabel.after(1000, add_one_second)
    mainWin.mainloop()

def restart(gameboard, gameboardState, gameFrame):
    for i in range(len(gameboard)):
        for ii in range(len(gameboard[i])):
            gameboard[i][ii] = "C"
            gameboardState[i][ii] = "H"
    for widget in gameFrame.winfo_children():
        widget.destroy()
    reveal_funcs.makeButtons(gameboard, gameFrame, gameboardButtons, gameboardState)
    timeLabel.configure(text="00")
    timeLabel.after(1000, add_one_second)
    completionLabel.forget()

def check_for_minute(time):
    index = 0
    time.reverse()
    for timeChecker in time:
        if timeChecker == "60" and index != len(time)-1:
            time[index] = "00"
            time[index+1] = str(int(time[index+1])+1)
        elif timeChecker == "60" and index == len(time)-1:
            time[index] = "00"
            time.append("1")
        else:
            index += 1
    time.reverse()
    return time

def add_one_second():
    hiddenLeft = False
    for i in gameboardState:
        if "H" in i:
            hiddenLeft = True
            break
    if hiddenLeft == False:
        completionLabel.pack()
        return
    else:
        currTime = timeLabel["text"].split(":")
        currTime[-1] = str(int(currTime[-1])+1)
        currTime = check_for_minute(currTime)
        for i in range(len(currTime)):
            if len(currTime[i]) == 1:
                currTime[i] = f"0{currTime[i]}"
        timeLabel.configure(text=":".join(currTime))
        timeLabel.after(1000, add_one_second)

def win():
    for i in range(len(gameboardState)):
        for ii in range(len(gameboardState[i])):
            gameboardState[i][ii] = "S"

main()