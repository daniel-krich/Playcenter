import tkinter as tk
import os
import random
from tkinter import messagebox

if os.path.exists('database/word_game.txt'):
    file = open('database/word_game.txt', mode="r", encoding="utf-8")
    word_bank = file.read().splitlines()
    file.close()
else:
    file = open('database/word_game.txt', mode="a", encoding="utf-8")
    file.close()
    word_bank = []


answer = ""


def set_answer(seq):
    global answer
    answer = seq
    return True


def play():
    global word_bank
    app = tk.Tk()
    app.eval('tk::PlaceWindow . center')
    app.geometry('350x170')
    app.resizable(False, False)
    app.title('השלם את המילה')
    random_word = random.choice(word_bank)[::-1]
    random_index = random.randint(0, len(random_word)-2)+1
    for idx in range(len(random_word)):
        if idx == random_index:
            word_input = tk.Entry(app, bg='#212121', fg='#fff', font=('Calibri', 13), width=1)
            word_input.place(relx=(0.5-(len(random_word)/25)/2)+(idx/25), rely=0.3, anchor=tk.CENTER)
        else:
            tk.Label(app, font=('Calibri', 13, 'bold'), text=random_word[idx]).place(relx=(0.5-(len(random_word)/25)/2)+(idx/25), rely=0.3, anchor=tk.CENTER)

    submit_button = tk.Button(app, text='שלח', bg='#6699ff', font=('Calibri', 11, 'bold'), width=350,
                                 command=lambda: app.destroy() if set_answer(word_input.get()) else None)
    submit_button.place(relx=0.5, rely=0.8, anchor=tk.CENTER)
    app.bind('<KeyPress>', lambda e: submit_button.invoke() if e.keycode == 13 else None)
    app.protocol("WM_DELETE_WINDOW", lambda: exit() if messagebox.askokcancel("יציאה", "?אתם בטוחים שאתם רוצים לצאת") else None)
    app.mainloop()
    if random_word[random_index] == answer:
        return {
            "points": 10,
            "type": 0,
            "title": "הצלחתם",
            "msg": "עבודה טובה, המילה הייתה {0}\n הרווחתם 10 נקודות".format(random_word[::-1])
        }
    else:
        return {
            "points": 0,
            "type": 2,
            "title": "טעיתם",
            "msg": "טעיתם במילה ולא הרווחתם כלום, המילה הייתה {0}".format(random_word[::-1])
        }
