import tkinter as tk
from tkinter import messagebox
import random

board = [[" "] * 3, [" "] * 3, [" "] * 3]
player = ""


def set_player(pl):
    global player
    player = pl


def choose_player():
    app = tk.Tk()
    app.eval('tk::PlaceWindow . center')
    app.geometry('300x100')
    app.resizable(False, False)
    app.title('איקס עיגול')
    tk.Label(app, text="בחרו איקס או עיגול", fg='#00994d', font=('Helvetica', 11, 'bold')).place(relx=0.5, rely=0.1, anchor=tk.CENTER)
    x_button = tk.Button(app, text='X', bg='#6699ff', fg='#fff', width=5, font=('Helvetica', 11, 'bold'), command=lambda: app.destroy() or set_player('X'))
    x_button.place(relx=0.4, rely=0.5, anchor=tk.CENTER)
    o_button = tk.Button(app, text='O', bg='#6699ff', fg='#fff', width=5, font=('Helvetica', 11, 'bold'), command=lambda: app.destroy() or set_player('O'))
    o_button.place(relx=0.6, rely=0.5, anchor=tk.CENTER)
    app.protocol("WM_DELETE_WINDOW", lambda: exit() if messagebox.askokcancel("יציאה", "?אתם בטוחים שאתם רוצים לצאת") else None)
    app.mainloop()


def clear(lines):
    for x in range(lines):
        print("\n")


def make_move(x, y):
    global board
    global player
    board[x][y] = player
    # print(x, y)


def display_table():
    global board
    global player
    app = tk.Tk()
    app.eval('tk::PlaceWindow . center')
    app.geometry('240x212')
    app.resizable(False, False)
    app.title('איקס עיגול')
    for x in range(len(board)):
        tk.Button(app, text=board[x][0], fg=('#33cc33' if board[x][0] == player else '#ff6600'), font=('Helvetica', 13, 'bold'), width=7, height=3, command=lambda inner_x=x: app.destroy() or (make_move(inner_x, 0) if board[inner_x][0] == " " else display_table())).grid(row=x, column=0)
        tk.Button(app, text=board[x][1], fg=('#33cc33' if board[x][1] == player else '#ff6600'), font=('Helvetica', 13, 'bold'), width=7, height=3, command=lambda inner_x=x: app.destroy() or (make_move(inner_x, 1) if board[inner_x][1] == " " else display_table())).grid(row=x, column=1)
        tk.Button(app, text=board[x][2], fg=('#33cc33' if board[x][2] == player else '#ff6600'), font=('Helvetica', 13, 'bold'), width=7, height=3, command=lambda inner_x=x: app.destroy() or (make_move(inner_x, 2) if board[inner_x][2] == " " else display_table())).grid(row=x, column=2)
    app.protocol("WM_DELETE_WINDOW", lambda: exit() if messagebox.askokcancel("יציאה", "?אתם בטוחים שאתם רוצים לצאת") else None)
    app.mainloop()


def play():
    global board
    global player
    choose_player()
    board = [[" "] * 3, [" "] * 3, [" "] * 3]
    if random.randint(1, 3) == 1:  # chance for the bot to start first
        bot_move("X" if player == "O" else "O")
    display_table()
    while len(check()) == 0:
        bot_move("X" if player == "O" else "O")
        if len(check()) == 0:
            display_table()

    return {
            "points": 10,
            "type": 0,
            "title": "ניצחון",
            "msg": "כל הכבוד, ניצחתם וזכיתם ב-10 נקודות"
        } if check() == player else {
            "points": 2,
            "type": 1,
            "title": "שווין",
            "msg": "הרווחתם 2 נקודות על שוויון"
        } if check() == "T" else {
            "points": 0,
            "type": 2,
            "title": "הפסד",
            "msg": "הפסדתם ולא הרווחתם ניקוד"
        }


def bot_move(bot_player_char):
    global board
    attack_res = bot_move_attack(bot_player_char)
    if attack_res is not None:
        board[attack_res[0]][attack_res[1]] = bot_player_char
        # print("228 bot move {0} {1}".format(attack_res[0], attack_res[1]))
        # clear(1)
        return
    for x in range(len(board)):
        for y in range(len(board)):
            if board[x][y] == bot_player_char:
                if board[x + 1 if x + 1 <= 2 else 2][y + 1 if y + 1 <= 2 else 2] == " " and x == y == 0:
                    board[x + 1 if x + 1 <= 2 else 2][y + 1 if y + 1 <= 2 else 2] = bot_player_char
                    # print("1 bot move {0} {1}".format(x + 1 if x + 1 <= 2 else 2, y + 1 if y + 1 <= 2 else 2))
                    # clear(1)
                    return

                if board[x - 1 if x - 1 >= 0 else 0][y + 1 if y + 1 <= 2 else 2] == " " \
                        and (x-1 == y+1 or (y+1)-(x-1) == 2):
                    board[x - 1 if x - 1 >= 0 else 0][y + 1 if y + 1 <= 2 else 2] = bot_player_char
                    # print("2 bot move {0} {1}".format(x - 1 if x - 1 >= 0 else 0, y + 1 if y + 1 <= 2 else 2))
                    # clear(1)
                    return

                if board[x - 1 if x - 1 >= 0 else 0][y - 1 if y - 1 >= 0 else 0] == " " and x == y == 2:
                    board[x - 1 if x - 1 >= 0 else 0][y - 1 if y - 1 >= 0 else 0] = bot_player_char
                    # print("3 bot move {0} {1}".format(x - 1 if x - 1 >= 0 else 0, y - 1 if y - 1 >= 0 else 0))
                    # clear(1)
                    return

                if board[x + 1 if x + 1 <= 2 else 2][y - 1 if y - 1 >= 0 else 0] == " " \
                        and (x+1 == y-1 or (x+1)-(y-1) == 2):
                    board[x + 1 if x + 1 <= 2 else 2][y - 1 if y - 1 >= 0 else 0] = bot_player_char
                    # print("4 bot move {0} {1}".format(x + 1 if x + 1 <= 2 else 2, y - 1 if y - 1 >= 0 else 0))
                    # clear(1)
                    return

                if board[x][y + 1 if y + 1 <= 2 else 2] == " ":
                    board[x][y + 1 if y + 1 <= 2 else 2] = bot_player_char
                    # print("5 bot move {0} {1}".format(x, y + 1 if y + 1 <= 2 else 2))
                    # clear(1)
                    return

                if board[x][y - 1 if y - 1 >= 0 else 0] == " ":
                    board[x][y - 1 if y - 1 >= 0 else 0] = bot_player_char
                    # print("6 bot move {0} {1}".format(x, y - 1 if y - 1 >= 0 else 0))
                    # clear(1)
                    return

                if board[x + 1 if x + 1 <= 2 else 2][y] == " ":
                    board[x + 1 if x + 1 <= 2 else 2][y] = bot_player_char
                    # print("7 bot move {0} {1}".format(x + 1 if x + 1 <= 2 else 2, y))
                    # clear(1)
                    return

                if board[x - 1 if x - 1 >= 0 else 0][y] == " ":
                    board[x - 1 if x - 1 >= 0 else 0][y] = bot_player_char
                    # print("8 bot move {0} {1}".format(x - 1 if x - 1 >= 0 else 0, y))
                    # clear(1)
                    return

    while True:
        rand_move_1 = random.randint(0, len(board)-1)
        rand_move_2 = random.randint(0, len(board)-1)
        if board[rand_move_1][rand_move_2] == " ":
            board[rand_move_1][rand_move_2] = bot_player_char
            # print("bot move random {0} {1}".format(rand_move_1, rand_move_2))
            # clear(1)
            break
    return


def bot_move_attack(bot_player_char):
    global board
    for x in range(len(board)):
        if board[x].count(bot_player_char) > 1 and " " in board[x]:  # attack
            return [x, board[x].index(" ")]

    for x in range(len(board)):
        temp_array = [board[0][x], board[1][x], board[2][x]]
        if temp_array.count(bot_player_char) > 1 and " " in temp_array:  # attack
            return [temp_array.index(" "), x]

    temp_array_left_right = [board[0][0], board[1][1], board[2][2]]
    temp_array_right_left = [board[0][2], board[1][1], board[2][0]]

    if temp_array_left_right.count(bot_player_char) > 1 and " " in temp_array_left_right:  # attack
        return [temp_array_left_right.index(" "), temp_array_left_right.index(" ")]

    if temp_array_right_left.count(bot_player_char) > 1 and " " in temp_array_right_left:  # attack
        res = temp_array_right_left.index(" ")
        if res == 0:
            return [0, 2]
        elif res == 1:
            return [1, 1]
        elif res == 2:
            return [2, 0]

    for x in range(len(board)):
        if board[x].count("X" if bot_player_char == "O" else "O") > 1 and " " in board[x]:  # defence
            return [x, board[x].index(" ")]

    for x in range(len(board)):
        temp_array = [board[0][x], board[1][x], board[2][x]]
        if temp_array.count("X" if bot_player_char == "O" else "O") > 1 and " " in temp_array:  # defence
            return [temp_array.index(" "), x]

    if temp_array_left_right.count(
            "X" if bot_player_char == "O" else "O") > 1 and " " in temp_array_left_right:  # defence
        return [temp_array_left_right.index(" "), temp_array_left_right.index(" ")]

    if temp_array_right_left.count(
            "X" if bot_player_char == "O" else "O") > 1 and " " in temp_array_right_left:  # defence
        res = temp_array_right_left.index(" ")
        if res == 0:
            return [0, 2]
        elif res == 1:
            return [1, 1]
        elif res == 2:
            return [2, 0]

    return None


def check() -> str:
    global board
    for x in range(len(board)):
        if board[x][0] == board[x][1] == board[x][2] != " ":
            return board[x][0]

    for x in range(len(board)):
        if board[0][x] == board[1][x] == board[2][x] != " ":
            return board[0][x]

    if board[0][0] == board[1][1] == board[2][2] != " " or board[0][2] == board[1][1] == board[2][0] != " ":
        return board[1][1]

    if board[0].count(" ") == 0 and board[1].count(" ") == 0 and board[2].count(" ") == 0:
        return "T"

    return ""
