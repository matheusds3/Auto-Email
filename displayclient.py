from tkinter import *
from tkinter import ttk
from functools import partial
from MySQLFunctions import *




#a = Tk()


class Display():
    def __init__(self, tela):
        self.tela = tela
        self.screen()
        self.screen_frame()
        self.widgets_frame()

        tela.mainloop()

    def screen(self):
        self.tela.geometry("400x300")
        self.tela.title("Auto-Email")
        self.tela.configure(background="#f8f8ff")
        self.tela.resizable(False, False)

    def screen_frame(self):
        self.frame = Frame(self.tela, bd=2, bg="#808080", highlightbackground="#f5f5f5", highlightthickness=1)
        self.frame.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)

    def widgets_frame(self):
        self.user = Label(self.frame, text="Usuário: ", bd=2, bg="#808080",
                          fg="black", font=("verdana", 8, "bold"))
        self.user.place(relx=0.3, rely=0.2, relwidth=0.2, relheight=0.1)
        self.user_name = Entry(self.frame)
        self.user_name.place(relx=0.3, rely=0.3, relwidth=0.4, relheight=0.1)
        self.password = Label(self.frame, text="Senha: ", bd=2, bg="#808080",
                              fg="black", font=("verdana", 8, "bold"))
        self.password.place(relx=0.3, rely=0.4, relwidth=0.2, relheight=0.1)
        self.password_entry = Entry(self.frame, show="*")
        self.password_entry.place(relx=0.3, rely=0.5, relwidth=0.4, relheight=0.1)
        self.ok = Button(self.frame, text="Entrar", bd=2,
                         bg="#f8f8ff", fg="black", font=("verdana", 8, "bold"), command=self.funcs)
        self.ok.place(relx=0.4, rely=0.8, relwidth=0.2, relheight=0.1)

    def funcs(self):
        Sqlfuncs('127.0.0.1', 'empresas', f'{self.user_name.get()}', f'{self.password_entry.get()}').conecta()







#808080


#Display(a)
