import playcenter.oron_games as math_games
import playcenter.accounts as data
import playcenter.ticktacktoe as ticktacktoe
import playcenter.word_game as word_game
import tkinter as tk
from tkinter import messagebox

users = data.Accounts("database/accounts.db")


def prompt_game_status(lst_result):
    users.current.points += lst_result['points']
    users.current.save()
    root = tk.Tk()
    root.withdraw()
    if lst_result['type'] == 0:
        messagebox.showinfo(lst_result['title'], lst_result['msg'])
    elif lst_result['type'] == 1:
        messagebox.showwarning(lst_result['title'], lst_result['msg'])
    else:
        messagebox.showerror(lst_result['title'], lst_result['msg'])
    root.destroy()
    menu_signed_in()


def menu_games():
    app = tk.Tk()
    app.eval('tk::PlaceWindow . center')
    app.geometry('350x190')
    app.resizable(False, False)
    app.title('משחקים')
    tk.Label(app, text="\t\tבחרו משחק לטעמכם\t\t\t\n\n", fg='#00994d', font=('Helvetica', 11, 'bold')).pack(side=tk.TOP)
    back_button = tk.Button(app, text='חזור', bg='#cecece', font=('Calibri', 11, 'bold'), width=350, command=lambda: app.destroy() or menu_signed_in())
    back_button.pack(side=tk.BOTTOM)
    math_game_button = tk.Button(app, text='משחקי חשבון', bg='#6699ff', font=('Calibri', 11, 'bold'), width=350, command=lambda: app.destroy() or prompt_game_status(math_games.play_math_random()))
    math_game_button.pack(side=tk.BOTTOM)
    ticktacktoe_button = tk.Button(app, text='איקס עיגול', bg='#6699ff', font=('Calibri', 11, 'bold'), width=350, command=lambda: app.destroy() or prompt_game_status(ticktacktoe.play()))
    ticktacktoe_button.pack(side=tk.BOTTOM)
    words_game_button = tk.Button(app, text='השלם את המילה', bg='#6699ff', font=('Calibri', 11, 'bold'), width=350, command=lambda: app.destroy() or prompt_game_status(word_game.play()))
    words_game_button.pack(side=tk.BOTTOM)
    app.protocol("WM_DELETE_WINDOW", lambda: exit() if messagebox.askokcancel("יציאה", "?אתם בטוחים שאתם רוצים לצאת") else None)
    app.mainloop()


def change_pass_wnd():
    app = tk.Tk()
    app.eval('tk::PlaceWindow . center')
    app.geometry('350x170')
    app.resizable(False, False)
    app.title('שינוי סיסמה')
    password_label = tk.Label(app, text="סיסמה", font=('Calibri', 11, 'bold')).grid(row=0, column=0)
    password_input = tk.Entry(app, width=45)
    password_input.grid(row=0, column=1)
    password_repeat_label = tk.Label(app, text="שוב סיסמה", font=('Calibri', 11, 'bold')).grid(row=1, column=0)
    password_repeat_input = tk.Entry(app, width=45)
    password_repeat_input.grid(row=1, column=1)
    change_pass_button = tk.Button(app, width=15, text='שנה סיסמה', bg='#6699ff', font=('Calibri', 11, 'bold'), command=lambda: messagebox.showinfo("הצלחה", "הסיסמה שונתה ל- {0}".format(password_input.get())) and app.destroy() and menu_signed_in() if users.change_pass(password_input.get(), password_repeat_input.get()) else messagebox.showerror("שגיאה", "הסיסמאות לא תואמות או קצרות מ-5 אותיות וספרות"))
    change_pass_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    back_button = tk.Button(app, text='חזור', bg='#cecece', font=('Calibri', 11, 'bold'), command=lambda: app.destroy() or menu_signed_in()).place(relx=0.5, rely=0.9, anchor=tk.CENTER)
    app.bind('<KeyPress>', lambda e: change_pass_button.invoke() if e.keycode == 13 else None)
    app.protocol("WM_DELETE_WINDOW", lambda: exit() if messagebox.askokcancel("יציאה", "?אתם בטוחים שאתם רוצים לצאת") else None)
    app.mainloop()


def delete_account_wnd():
    app = tk.Tk()
    app.eval('tk::PlaceWindow . center')
    app.geometry('350x170')
    app.resizable(False, False)
    app.title('מחיקת משתמש')
    user_label = tk.Label(app, text="שם משתמש", font=('Calibri', 11, 'bold')).grid(row=0, column=0)
    user_input = tk.Entry(app, width=45)
    user_input.grid(row=0, column=1)
    delete_button = tk.Button(app, width=15, text='מחק', bg='#ff6666', font=('Calibri', 11, 'bold'), command=lambda: messagebox.showinfo("הצלחה", "נמחק מהמבנה נתונים {0}".format(user_input.get())) and app.destroy() and menu_signed_in() if users.delete_user(user_input.get()) else messagebox.showerror("שגיאה", "המשתמש לא נמצא או שהזנתם את שם המשתמש שלכם"))
    delete_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    back_button = tk.Button(app, text='חזור', bg='#cecece', font=('Calibri', 11, 'bold'), command=lambda: app.destroy() or menu_signed_in()).place(relx=0.5, rely=0.9, anchor=tk.CENTER)
    app.bind('<KeyPress>', lambda e: delete_button.invoke() if e.keycode == 13 else None)
    app.protocol("WM_DELETE_WINDOW", lambda: exit() if messagebox.askokcancel("יציאה", "?אתם בטוחים שאתם רוצים לצאת") else None)
    app.mainloop()


def menu_signed_in():
    app = tk.Tk()
    app.eval('tk::PlaceWindow . center')
    if users.current.is_admin > 0:
        app.geometry('350x240')
    else:
        app.geometry('350x205')
    app.resizable(False, False)
    app.title("מחובר - {0} ({1})".format(users.current.username, users.current.id))
    logout_button = tk.Button(app, text='התנתקות', bg='#ff9966', font=('Calibri', 11, 'bold'), width=350, command=lambda: app.destroy() or users.logout())
    logout_button.pack(side=tk.BOTTOM)
    if users.current.is_admin > 0:
        delete_button = tk.Button(app, text='מחק משתמש', bg='#ff6666', font=('Calibri', 11, 'bold'), width=350, command=lambda: app.destroy() or delete_account_wnd())
        delete_button.pack(side=tk.BOTTOM)
    change_pass_button = tk.Button(app, text='שנה סיסמה', bg='#cecece', font=('Calibri', 11, 'bold'), width=350, command=lambda: app.destroy() or change_pass_wnd())
    change_pass_button.pack(side=tk.BOTTOM)
    games_button = tk.Button(app, text='משחקים', bg='#cecece', font=('Calibri', 11, 'bold'), width=350, command=lambda: app.destroy() or menu_games())
    games_button.pack(side=tk.BOTTOM)
    info_button = tk.Button(app, text='רענון', bg='#cecece', font=('Calibri', 11, 'bold'), width=350, command=lambda: app.destroy() or menu_signed_in())
    info_button.pack(side=tk.BOTTOM)
    account_info_label = tk.Label(app, font=('Calibri', 11, 'bold'), text="ID: {0}\nName: {1}\nAdmin: {2}\nPoints: {3}".format(users.current.id, users.current.username, "Yes" if users.current.is_admin > 0 else "No", users.current.points))
    account_info_label.pack(side=tk.TOP)
    app.protocol("WM_DELETE_WINDOW", lambda: exit() if messagebox.askokcancel("יציאה", "?אתם בטוחים שאתם רוצים לצאת") else None)
    app.mainloop()


def login_wnd():
    app = tk.Tk()
    app.eval('tk::PlaceWindow . center')
    app.geometry('350x170')
    app.resizable(False, False)
    app.title('התחברות')
    username_label = tk.Label(app, text="שם משתמש", font=('Calibri', 11, 'bold')).grid(row=0, column=0)
    username_input = tk.Entry(app, width=45)
    username_input.grid(row=0, column=1)
    password_label = tk.Label(app, text="סיסמה", font=('Calibri', 11, 'bold')).grid(row=1, column=0)
    password_input = tk.Entry(app, width=45)
    password_input.grid(row=1, column=1)
    login_button = tk.Button(app, text='התחברות', bg='#6699ff', font=('Calibri', 11, 'bold'), width=10, command=lambda: app.destroy() and menu_signed_in() if users.login(username_input.get(), password_input.get()) else messagebox.showerror("שגיאה", "שם המשתמש או הסיסמה שגויים"))
    login_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    back_button = tk.Button(app, text='חזור', bg='#cecece', font=('Calibri', 11, 'bold'), command=lambda: app.destroy() or menu_signed_out()).place(relx=0.5, rely=0.9, anchor=tk.CENTER)
    app.bind('<KeyPress>', lambda e: login_button.invoke() if e.keycode == 13 else None)
    app.protocol("WM_DELETE_WINDOW", lambda: exit() if messagebox.askokcancel("יציאה", "?אתם בטוחים שאתם רוצים לצאת") else None)
    app.mainloop()


def register_wnd():
    app = tk.Tk()
    app.eval('tk::PlaceWindow . center')
    app.geometry('350x170')
    app.resizable(False, False)
    app.title('הרשמה')
    username_label = tk.Label(app, text="שם משתמש", font=('Calibri', 11, 'bold')).grid(row=0, column=0)
    username_input = tk.Entry(app, width=45)
    username_input.grid(row=0, column=1)
    password_label = tk.Label(app, text="סיסמה", font=('Calibri', 11, 'bold')).grid(row=1, column=0)
    password_input = tk.Entry(app, width=45)
    password_input.grid(row=1, column=1)
    password_repeat_label = tk.Label(app, text="שוב סיסמה", font=('Calibri', 11, 'bold')).grid(row=2, column=0)
    password_repeat_input = tk.Entry(app, width=45)
    password_repeat_input.grid(row=2, column=1)
    register_button = tk.Button(app, text='הרשמה', bg='#00cc66', font=('Calibri', 11, 'bold'), width=10, command=lambda: app.destroy() and menu_signed_in() if users.insert_user(username_input.get(), password_input.get(), password_repeat_input.get()) else messagebox.showerror("שגיאה", "המשתמש קיים או שהסיסמאות או השם לא תקינים"))
    register_button.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
    back_button = tk.Button(app, text='חזור', bg='#cecece', font=('Calibri', 11, 'bold'), command=lambda: app.destroy() or menu_signed_out()).place(relx=0.5, rely=0.9, anchor=tk.CENTER)
    app.bind('<KeyPress>', lambda e: register_button.invoke() if e.keycode == 13 else None)
    app.protocol("WM_DELETE_WINDOW", lambda: exit() if messagebox.askokcancel("יציאה", "?אתם בטוחים שאתם רוצים לצאת") else None)
    app.mainloop()


def menu_signed_out():
    app = tk.Tk()
    app.eval('tk::PlaceWindow . center')
    app.geometry('350x150')
    app.resizable(False, False)
    app.title('מרכז המשחקים')
    tk.Label(app, text="ברוכים הבאים למרכז המשחקים", fg='#e67300', font=('Helvetica', 11, 'bold')).place(relx=0.5, rely=0.2, anchor=tk.CENTER)
    tk.Label(app, text="להמשך אנא התחברו או הירשמו", fg='#000', font=('Helvetica', 10)).place(relx=0.5, rely=0.35, anchor=tk.CENTER)
    register_button = tk.Button(app, text='הרשמה', bg='#cecece', font=('Calibri', 11, 'bold'), width=100, command=lambda: app.destroy() or register_wnd())
    register_button.pack(side=tk.BOTTOM)
    login_button = tk.Button(app, text='התחברות', bg='#6699ff', width=100, font=('Calibri', 11, 'bold'), command=lambda: app.destroy() or login_wnd())
    login_button.pack(side=tk.BOTTOM)
    app.protocol("WM_DELETE_WINDOW", lambda: exit() if messagebox.askokcancel("יציאה", "?אתם בטוחים שאתם רוצים לצאת") else None)
    app.mainloop()


def menu():
    if users.current is not None:
        menu_signed_in()
    else:
        menu_signed_out()
    menu()


if __name__ == '__main__':
    menu()

