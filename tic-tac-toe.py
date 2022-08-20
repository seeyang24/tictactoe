from tkinter import *
import random


def next_turn(row, column):
    global player
    
    # check to see if the button we click on is empty and there is no winner
    if buttons[row][column]['text'] == "" and check_winner() is False:
        # if player is equal to first player
        if player == players[0]:
            # player 1 chooses his position on grid
            buttons[row][column]['text'] = player
            # if no winner, it will display that that is player 2's turn
            if check_winner() is False:
                player = players[1]
                label.config(text=(players[1]+ "turn"))
            elif check_winner() is True:
                label.config(text=(players[0] + " wins!"))
            elif check_winner() == 'Tie':
                label.config(text=("Tie."))
        else:
            # player 2 chooses his position on grid
            buttons[row][column]['text'] = player
            # if no winner, it will display that that is player 2's turn
            if check_winner() is False:
                player = players[0]
                label.config(text=(players[0]+ "turn"))
            elif check_winner() is True:
                label.config(text=(players[1] + " wins!"))
            elif check_winner() == "Tie":
                label.config(text="Tie!")

def check_winner():
    # ROW
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            return True
    # Column
    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            return True
    # Diagnol
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        return True
    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        return True
    # TIE
    elif empty_spaces() is False:
        return "Tie"
    else:
        return False

def empty_spaces():
    spaces = 9
    
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -= 1
    # No spaces left
    if spaces == 0:
        return False
    else:
        return True

def new_game():
    global player
    # randomize the players
    player = random.choice(players)
    
    label.config(text=player + " turn")
    
    # set all buttons to an empty string
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="")

# Window
window = Tk()
window.title("Tic-Tac-Toe")
players = ["x", "o"]
player = random.choice(players)
buttons = [[0,0,0], 
           [0,0,0],
           [0,0,0]]

label = Label(text=player + " turn", font=('consolas',40))
label.pack(side="top")

reset_button = Button(text="Restart", font=('consolas',20), command=new_game)
reset_button.pack(side="top")

frame = Frame(window)
frame.pack()

# 3 rows and 3 columns
for row in range(3):
    for column in range(3):
        # add buttons to frame, and frame to window
        buttons[row][column] = Button(frame, text="",font=('consolas',40), width=5, height=2,
                                      command= lambda row=row, column=column: next_turn(row,column))
        buttons[row][column].grid(row=row,column=column)
        
window.mainloop()