import tkinter

def set_tile(row, column):
    global curr_player
    if board[row][column]["text"]!="":
        #already taken the spot
        return
    board[row][column]["text"]=curr_player
    if(curr_player==playerO):
        curr_player=playerX
    else:
        curr_player=playerO
    label["text"]=curr_player+" 's turn"
    check_winner()
    def check_winner():
        global turns,game_over
        turns+=1
        #horizontally, check 3 rows
        for row in range(3):
            if(board[row][0]["text"]==board[row][1]["text"]==board[row][2]["text"]
            and board[row][0]["text"]!=""):
            label.config(text=board[row][0]["text"]+" is the winner!",foreground=color_yellow)
            for column in range(3):
                board[row][column].config(foreground=color_yellow,background=color_light_gray)
            game_over=True
            return

def new_game():
    pass

playerO = "O"
playerX = "X"
curr_player = playerX 
board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

color_blue = "#4584b6"
color_yellow = "#ffde57"
color_gray = "#343434"
color_light_gray = "#646464"
turns=0
game_over=False
window = tkinter.Tk()
window.title("Tic Tac Toe")
window.resizable(False, False)

frame = tkinter.Frame(window)
label = tkinter.Label(frame, text=curr_player + "'s turn", font=("Consolas", 20),
                      background=color_gray, foreground="white")
label.grid(row=0, column=0, columnspan=3, sticky="we")

for row in range(3):
    for column in range(3):
        board[row][column] = tkinter.Button(frame, text="", font=("Consolas", 50, "bold"),
                                            background=color_gray, foreground=color_blue, width=4, height=1,
                                            command=lambda row=row, column=column: set_tile(row, column))
        board[row][column].grid(row=row + 1, column=column)

button = tkinter.Button(frame, text="Restart", font=("Consolas", 20), background=color_gray,
                        foreground="white", command=new_game)
button.grid(row=4, column=0, columnspan=3, sticky="we")

frame.pack()

#center the window
window.update()
window_width=window.winfo_width()
window_height=window.winfo_height()
screen_width=window.winfo_screenwidth()
screen_height=window.winfo_screenheight()
window_x=int((screen_width/2)-(window_width/2))
window_y=int((screen_height/2)-(screen_height/2))
#format
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")
window.mainloop()
