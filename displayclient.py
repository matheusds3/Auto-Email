from tkinter import *
from tkinter import messagebox
from MySQLFunctions import *


# Tela Inicial

class Display():
    def __init__(self, tela):
        self.tela = tela
        self.screen()
        self.screen_frame()
        self.widgets_frame()
        tela.mainloop()


    def screen(self):
        self.tela.geometry("400x300+760+300")
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
        self.user_entry = Entry(self.frame)
        self.user_entry.place(relx=0.3, rely=0.3, relwidth=0.4, relheight=0.1)
        self.password = Label(self.frame, text="Senha: ", bd=2, bg="#808080",
                              fg="black", font=("verdana", 8, "bold"))
        self.password.place(relx=0.3, rely=0.4, relwidth=0.2, relheight=0.1)
        self.password_entry = Entry(self.frame, show="*")
        self.password_entry.place(relx=0.3, rely=0.5, relwidth=0.4, relheight=0.1)
        self.ok = Button(self.frame, text="Entrar", bd=2,
                         bg="#f8f8ff", fg="black", font=("verdana", 8, "bold"), command=self.funcs)
        self.ok.place(relx=0.4, rely=0.7, relwidth=0.2, relheight=0.1)
        self.py = Label(self.frame, text=".py Miku©", bd=2, bg="#808080",
                          fg="black", font=("verdana", 6, "bold"))
        self.py.place(relx=0.85, rely=0.94, relwidth=0.15, relheight=0.05)

    def funcs(self):
        self.hosting = Sqlfuncs('127.0.0.1', 'empresas',
                                f'{self.user_entry.get()}', f'{self.password_entry.get()}').conecta()
        if self.hosting[1] == True:
            print('True')
            self.close()
            self.retorna()

        else:
            messagebox.showerror("Error", "Dados Incorretos!")
            self.limpar()
    def close(self):
        self.tela.quit()
        #.quit() fecha a tela, mas continua em execução
        #.destroy() apaga a tela e sai do programa
    def limpar(self):
        self.user_entry.delete(0,END)
        self.password_entry.delete(0, END)
    def retorna(self):
        return self.user_entry.get(), self.password_entry.get(), self.hosting[0]

# Tela de Opções

class Display2:
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
        self.acao = Label(self.frame, text="Selecione uma opção: ", bd=2, bg="#808080",
                          fg="black", font=("verdana", 10, "bold"))
        self.acao.place(relx=0.2, rely=0.05, relwidth=0.6, relheight=0.1)

        self.cadastrar = Button(self.frame, text="Cadastrar", bd=2, bg="#f8f8ff",
                          fg="black", font=("verdana", 8, "bold"), command=self.cadastro)
        self.cadastrar.place(relx=0.3, rely=0.15, relwidth=0.4, relheight=0.15)

        self.atualizar = Button(self.frame, text="Atualizar", bd=2, bg="#f8f8ff",
                              fg="black", font=("verdana", 8, "bold"), command=self.atualiza)
        self.atualizar.place(relx=0.3, rely=0.3, relwidth=0.4, relheight=0.15)

        self.consultar = Button(self.frame, text="Consultar", bd=2,
                         bg="#f8f8ff", fg="black", font=("verdana", 8, "bold"), command=self.consulta)
        self.consultar.place(relx=0.3, rely=0.45, relwidth=0.4, relheight=0.15)

        self.deletar = Button(self.frame, text="Deletar", bd=2,
                                bg="#f8f8ff", fg="black", font=("verdana", 8, "bold"), command=self.deleta)
        self.deletar.place(relx=0.3, rely=0.6, relwidth=0.4, relheight=0.15)

        self.enviar = Button(self.frame, text="Enviar", bd=2,
                              bg="#f8f8ff", fg="black", font=("verdana", 8, "bold"), command=self.envia)
        self.enviar.place(relx=0.3, rely=0.75, relwidth=0.4, relheight=0.15)

        self.py = Label(self.frame, text=".py Miku©", bd=2, bg="#808080",
                        fg="black", font=("verdana", 6, "bold"))
        self.py.place(relx=0.85, rely=0.94, relwidth=0.15, relheight=0.05)

        self.sair = Button(self.frame, text="Desconectar", bd=2, bg="#f8f8ff",
                        fg="black", font=("verdana", 6, "bold"), command=self.sair)
        self.sair.place(relx=0.4, rely=0.92, relwidth=0.2, relheight=0.06)

    def sair(self):
        self.ret = 6
        self.close()
        return self.ret
    def close(self):
        self.tela.quit()
        #.quit() fecha a tela, mas continua em execução
        #.destroy() apaga a tela e sai do programa
    def cadastro(self):
        self.ret = 1
        self.close()
        return self.ret
    def atualiza(self):
        self.ret = 2
        self.close()
        return self.ret
    def consulta(self):
        self.ret = 3
        self.close()
        return self.ret
    def deleta(self):
        self.ret = 4
        self.close()
        return self.ret
    def envia(self):
        self.ret = 5
        self.close()
        return self.ret
    def retornou(self):
        if self.ret == 1:
            return self.ret
        elif self.ret == 2:
            return self.ret
        elif self.ret == 3:
            return self.ret
        elif self.ret == 4:
            return self.ret
        elif self.ret == 5:
            return self.ret
        elif self.ret == 6:
            return self.ret

# Display de Cadastro

class DisplayCadastrar:
    def __init__(self, tela, user_entry, password_entry,con):
        self.tela = tela
        self.user_entry = user_entry
        self.password_entry = password_entry
        self.con = con
        self.screen_cadastro()
        self.screen_frame_cadastro()
        self.widgets_frame_cadastro()
        tela.mainloop()

    def screen_cadastro(self):
        self.tela.geometry("400x300")
        self.tela.title("Auto-Email")
        self.tela.configure(background="#f8f8ff")
        self.tela.resizable(False, False)

    def screen_frame_cadastro(self):
        self.frame = Frame(self.tela, bd=2, bg="#808080", highlightbackground="#f5f5f5", highlightthickness=1)
        self.frame.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)

    def widgets_frame_cadastro(self):
        self.cadastro_nome = Label(self.frame, text="Digite o nome: ", bd=2, bg="#808080",
                                   fg="black", font=("verdana", 10, "bold"))
        self.cadastro_nome.place(relx=0.05, rely=0.1, relwidth=0.6, relheight=0.1)

        self.cadastro_nome_entry = Entry(self.frame)
        self.cadastro_nome_entry.place(relx=0.2, rely=0.2, relwidth=0.6, relheight=0.1)

        self.dia = Label(self.frame, text="Digite o dia: ", bd=2, bg="#808080",
                                   fg="black", font=("verdana", 10, "bold"))
        self.dia.place(relx=0.02, rely=0.3, relwidth=0.6, relheight=0.1)

        self.dia_entry = Entry(self.frame)
        self.dia_entry.place(relx=0.2, rely=0.4, relwidth=0.6, relheight=0.1)

        self.email = Label(self.frame, text="Digite o E-mail: ", bd=2, bg="#808080",
                         fg="black", font=("verdana", 10, "bold"))
        self.email.place(relx=0.05, rely=0.5, relwidth=0.6, relheight=0.1)

        self.email_entry = Entry(self.frame)
        self.email_entry.place(relx=0.2, rely=0.6, relwidth=0.6, relheight=0.1)

        self.cadastrar = Button(self.frame, text="Cadastrar Dado", bd=2,
                              bg="#f8f8ff", fg="black", font=("verdana", 8, "bold"), command=self.funcs_cadastro)
        self.cadastrar.place(relx=0.3, rely=0.8, relwidth=0.4, relheight=0.1)

        self.py = Label(self.frame, text=".py Miku©", bd=2, bg="#808080",
                        fg="black", font=("verdana", 6, "bold"))
        self.py.place(relx=0.85, rely=0.94, relwidth=0.15, relheight=0.05)

    def funcs_cadastro(self):

        Sqlfuncs('127.0.0.1', 'empresas', f'{self.user_entry}',
                 f'{self.password_entry}').cadastrar(self.con, 'empresas_datas', 'nome_empresa', self.cadastro_nome_entry.get(), self.dia_entry.get(), self.email_entry.get())
        self.close()

    def close(self):
        self.tela.quit()

# Display Atualizar

class DisplayAtualizar:
    def __init__(self, tela, user_entry, password_entry,con):
        self.tela = tela
        self.user_entry = user_entry
        self.password_entry = password_entry
        self.con = con
        self.screen_cadastro()
        self.screen_frame_cadastro()
        self.widgets_frame_cadastro()
        tela.mainloop()

    def screen_cadastro(self):
        self.tela.geometry("400x300")
        self.tela.title("Auto-Email")
        self.tela.configure(background="#f8f8ff")
        self.tela.resizable(False, False)

    def screen_frame_cadastro(self):
        self.frame = Frame(self.tela, bd=2, bg="#808080", highlightbackground="#f5f5f5", highlightthickness=1)
        self.frame.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)

    def widgets_frame_cadastro(self):
        self.id = Label(self.frame, text="Digite o ID: ", bd=2, bg="#808080",
                        fg="black", font=("verdana", 10, "bold"))
        self.id.place(relx=0.05, rely=0.1, relwidth=0.6, relheight=0.1)

        self.id_entry = Entry(self.frame)
        self.id_entry.place(relx=0.2, rely=0.2, relwidth=0.6, relheight=0.1)

        self.dado = Label(self.frame, text="Digite o dado a ser alterado: ", bd=2, bg="#808080",
                          fg="black", font=("verdana", 10, "bold"))
        self.dado.place(relx=0.02, rely=0.3, relwidth=0.6, relheight=0.1)

        self.dado_entry = Entry(self.frame)
        self.dado_entry.place(relx=0.2, rely=0.4, relwidth=0.6, relheight=0.1)

        self.novo_dado = Label(self.frame, text="Digite o novo dado: ", bd=2, bg="#808080",
                               fg="black", font=("verdana", 10, "bold"))
        self.novo_dado.place(relx=0.05, rely=0.5, relwidth=0.6, relheight=0.1)

        self.novo_dado_entry = Entry(self.frame)
        self.novo_dado_entry.place(relx=0.2, rely=0.6, relwidth=0.6, relheight=0.1)

        self.atualizar = Button(self.frame, text="Atualizar Dado", bd=2,
                                bg="#f8f8ff", fg="black", font=("verdana", 8, "bold"), command=self.funcs_atualiza)
        self.atualizar.place(relx=0.3, rely=0.8, relwidth=0.4, relheight=0.1)

        self.py = Label(self.frame, text=".py Miku©", bd=2, bg="#808080",
                        fg="black", font=("verdana", 6, "bold"))
        self.py.place(relx=0.85, rely=0.94, relwidth=0.15, relheight=0.05)

    def funcs_atualiza(self):

        Sqlfuncs('127.0.0.1', 'empresas', f'{self.user_entry}',
                 f'{self.password_entry}').atualizar(self.con, 'empresas_datas', 'id_empresa', self.id_entry.get(), self.dado_entry.get(), self.novo_dado_entry.get())
        self.close()

    def close(self):
        self.tela.quit()

# Display Consultar

class DisplayConsultar:
    def __init__(self, tela, user_entry, password_entry,con):
        self.tela = tela
        self.user_entry = user_entry
        self.password_entry = password_entry
        self.con = con
        self.screen_cadastro()
        self.screen_frame_cadastro()
        self.widgets_frame_cadastro()
        tela.mainloop()

    def screen_cadastro(self):
        self.tela.geometry("400x300")
        self.tela.title("Auto-Email")
        self.tela.configure(background="#f8f8ff")
        self.tela.resizable(False, False)

    def screen_frame_cadastro(self):
        self.frame = Frame(self.tela, bd=2, bg="#808080", highlightbackground="#f5f5f5", highlightthickness=1)
        self.frame.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)

    def widgets_frame_cadastro(self):
        self.nome = Label(self.frame, text="Digite o nome: ", bd=2, bg="#808080",
                          fg="black", font=("verdana", 10, "bold"))
        self.nome.place(relx=0.05, rely=0.1, relwidth=0.6, relheight=0.1)

        self.nome_entry = Entry(self.frame)
        self.nome_entry.place(relx=0.2, rely=0.2, relwidth=0.6, relheight=0.1)

        self.consultar = Button(self.frame, text="Consultar", bd=2,
                                bg="#f8f8ff", fg="black", font=("verdana", 8, "bold"), command=self.funcs_consulta)
        self.consultar.place(relx=0.3, rely=0.8, relwidth=0.4, relheight=0.1)

        self.py = Label(self.frame, text=".py Miku©", bd=2, bg="#808080",
                        fg="black", font=("verdana", 6, "bold"))
        self.py.place(relx=0.85, rely=0.94, relwidth=0.15, relheight=0.05)

    def funcs_consulta(self):

        Sqlfuncs('127.0.0.1', 'empresas', f'{self.user_entry}',
                 f'{self.password_entry}').consulta(self.con, 'empresas_datas', 'nome_empresa', self.nome_entry.get())
        self.close()

    def close(self):
        self.tela.quit()

# Display Deletar

class DisplayDeletar:
    def __init__(self, tela, user_entry, password_entry,con):
        self.tela = tela
        self.user_entry = user_entry
        self.password_entry = password_entry
        self.con = con
        self.screen_cadastro()
        self.screen_frame_cadastro()
        self.widgets_frame_cadastro()
        tela.mainloop()

    def screen_cadastro(self):
        self.tela.geometry("400x300")
        self.tela.title("Auto-Email")
        self.tela.configure(background="#f8f8ff")
        self.tela.resizable(False, False)

    def screen_frame_cadastro(self):
        self.frame = Frame(self.tela, bd=2, bg="#808080", highlightbackground="#f5f5f5", highlightthickness=1)
        self.frame.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)

    def widgets_frame_cadastro(self):
        self.id = Label(self.frame, text="Digite o ID: ", bd=2, bg="#808080",
                        fg="black", font=("verdana", 10, "bold"))
        self.id.place(relx=0.05, rely=0.1, relwidth=0.6, relheight=0.1)

        self.id_entry = Entry(self.frame)
        self.id_entry.place(relx=0.2, rely=0.2, relwidth=0.6, relheight=0.1)

        self.deletar = Button(self.frame, text="Deletar", bd=2,
                              bg="#f8f8ff", fg="black", font=("verdana", 8, "bold"), command=self.funcs_deleta)
        self.deletar.place(relx=0.3, rely=0.8, relwidth=0.4, relheight=0.1)

        self.py = Label(self.frame, text=".py Miku©", bd=2, bg="#808080",
                        fg="black", font=("verdana", 6, "bold"))
        self.py.place(relx=0.85, rely=0.94, relwidth=0.15, relheight=0.05)

    def funcs_deleta(self):


        Sqlfuncs('127.0.0.1', 'empresas', f'{self.user_entry}',
                 f'{self.password_entry}').deletar(self.con, 'empresas_datas', 'id_empresa', self.id_entry.get())

        self.close()

    def close(self):
        self.tela.quit()
