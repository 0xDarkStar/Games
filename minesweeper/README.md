# Minesweeper Game
This is a normal minesweeper game I made since I didn't want to download or play one online.
It has a fully functioning UI version and an unfinished terminal version.

## UI Version
This version is fully working and has most if not all features present in other normal minesweeper games.
Those features being:
-  Automatically revealing adjacent spaces
-  Safe first click (will always start on a space with no bombs around)
-  Flags
-  Restart button

## Terminal Version
This version is not working, at all.
It still needs additional logic to:
- read what spaces the player wants to reveal
- read what spaces the player wants to flag
- show only certain spaces
- print a board the user can actually play on (and not just the array from the code)


## Files
There are only four files, two of which are how you start the game.

The other two files ([mine_logic.py](https://github.com/0xDarkStar/Games/blob/main/minesweeper/mine_logic.py) and [reveal_funcs.py](https://github.com/0xDarkStar/Games/blob/main/minesweeper/reveal_funcs.py)) are for the logic handling board creation and checking user input against the board.

reveal_funcs.py currently is made for the UI version. Once I progress the terminal version, a new file will have to be made to check the user's input against the board.
