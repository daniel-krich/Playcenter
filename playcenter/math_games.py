import random as rand
import tkinter as tk
from tkinter import messagebox

answer = 0


def set_answer(ans):
    try:
        global answer
        answer = int(ans)
        return True
    except ValueError:
        return False


def play_math_plus():
    global answer
    num1 = rand.randint(10, 100)
    num2 = rand.randint(10, 100)
    app = tk.Tk()
    app.eval('tk::PlaceWindow . center')
    app.geometry('300x100')
    app.resizable(False, False)
    app.title('משחקי חשבון')
    math_label = tk.Label(app, font=('Helvetica', 11, 'bold'), text="{0} + {1} = ".format(num1, num2)).place(relx=0.35, rely=0.3, anchor=tk.CENTER)
    answer_input = tk.Entry(app, width=11)
    answer_input.place(relx=0.6, rely=0.3, anchor=tk.CENTER)
    math_game_submit_button = tk.Button(app, text='שלח', font=('Helvetica', 11, 'bold'), bg='#6699ff', width=30, command=lambda: app.destroy() if set_answer(answer_input.get()) else None)
    math_game_submit_button.place(relx=0.5, rely=0.7, anchor=tk.CENTER)
    app.bind('<KeyPress>', lambda e: math_game_submit_button.invoke() if e.keycode == 13 else None)
    app.protocol("WM_DELETE_WINDOW", lambda: exit() if messagebox.askokcancel("יציאה", "?אתם בטוחים שאתם רוצים לצאת") else None)
    app.mainloop()
    if num1 + num2 == answer:
        return {
            "points": 10,
            "type": 0,
            "title": "תשובה נכונה",
            "msg": "זכיתם ב-10 נקודות"
        }
    else:
        return {
            "points": 0,
            "type": 2,
            "title": "טעות",
            "msg": "התשובה הנכונה הייתה {0}".format(num1 + num2)
        }


def play_math_minus():
    global answer
    num1 = rand.randint(100, 200)
    num2 = rand.randint(10, 100)
    app = tk.Tk()
    app.eval('tk::PlaceWindow . center')
    app.geometry('300x100')
    app.resizable(False, False)
    app.title('משחקי חשבון')
    math_label = tk.Label(app, font=('Helvetica', 11, 'bold'), text="{0} - {1} = ".format(num1, num2)).place(relx=0.35, rely=0.3, anchor=tk.CENTER)
    answer_input = tk.Entry(app, width=11)
    answer_input.place(relx=0.6, rely=0.3, anchor=tk.CENTER)
    math_game_submit_button = tk.Button(app, text='שלח', font=('Helvetica', 11, 'bold'), bg='#6699ff', width=30, command=lambda: app.destroy() if set_answer(answer_input.get()) else None)
    math_game_submit_button.place(relx=0.5, rely=0.7, anchor=tk.CENTER)
    app.bind('<KeyPress>', lambda e: math_game_submit_button.invoke() if e.keycode == 13 else None)
    app.protocol("WM_DELETE_WINDOW", lambda: exit() if messagebox.askokcancel("יציאה", "?אתם בטוחים שאתם רוצים לצאת") else None)
    app.mainloop()
    if num1 - num2 == answer:
        return {
            "points": 10,
            "type": 0,
            "title": "תשובה נכונה",
            "msg": "זכיתם ב-10 נקודות"
        }
    else:
        return {
            "points": 0,
            "type": 2,
            "title": "טעות",
            "msg": "התשובה הנכונה הייתה {0}".format(num1 - num2)
        }


def play_math_multiplication():
    global answer
    num1 = rand.randint(1, 15)
    num2 = rand.randint(1, 15)
    app = tk.Tk()
    app.eval('tk::PlaceWindow . center')
    app.geometry('300x100')
    app.resizable(False, False)
    app.title('משחקי חשבון')
    math_label = tk.Label(app, font=('Helvetica', 11, 'bold'), text="{0} * {1} = ".format(num1, num2)).place(relx=0.35, rely=0.3, anchor=tk.CENTER)
    answer_input = tk.Entry(app, width=11)
    answer_input.place(relx=0.6, rely=0.3, anchor=tk.CENTER)
    math_game_submit_button = tk.Button(app, text='שלח', font=('Helvetica', 11, 'bold'), bg='#6699ff', width=30, command=lambda: app.destroy() if set_answer(answer_input.get()) else None)
    math_game_submit_button.place(relx=0.5, rely=0.7, anchor=tk.CENTER)
    app.bind('<KeyPress>', lambda e: math_game_submit_button.invoke() if e.keycode == 13 else None)
    app.protocol("WM_DELETE_WINDOW", lambda: exit() if messagebox.askokcancel("יציאה", "?אתם בטוחים שאתם רוצים לצאת") else None)
    app.mainloop()
    if num1 * num2 == answer:
        return {
            "points": 10,
            "type": 0,
            "title": "תשובה נכונה",
            "msg": "זכיתם ב-10 נקודות"
        }
    else:
        return {
            "points": 0,
            "type": 2,
            "title": "טעות",
            "msg": "התשובה הנכונה הייתה {0}".format(num1 * num2)
        }


def play_math_random():
    choice = rand.randint(1, 3)
    if choice == 1:
        return play_math_plus()
    elif choice == 2:
        return play_math_minus()
    elif choice == 3:
        return play_math_multiplication()
