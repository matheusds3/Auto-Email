from displayclient import *
from Emailconfig import *

# Programa Para Envio de E-mails Automáticos a Partir de um Banco de Dados MySQL

tela = Tk()

tela1 = Display(tela)
user_pass_and_con = tela1.retorna()

loop = 1
while loop != 0:
    tela2 = Display2(tela)
    opcao = tela2.retornou()

    if opcao == 1:
        DisplayCadastrar(tela, user_pass_and_con[0], user_pass_and_con[1], user_pass_and_con[2])
        loop = 1
    elif opcao == 2:
        DisplayAtualizar(tela, user_pass_and_con[0], user_pass_and_con[1], user_pass_and_con[2])
        loop = 1
    elif opcao == 3:
        DisplayConsultar(tela, user_pass_and_con[0], user_pass_and_con[1], user_pass_and_con[2])
        loop = 1
    elif opcao == 4:
        DisplayDeletar(tela, user_pass_and_con[0], user_pass_and_con[1], user_pass_and_con[2])
        loop = 1
    elif opcao == 5:
        Enviar("127.0.0.1", "empresas", user_pass_and_con[0], user_pass_and_con[1]).enviar()
        loop = 1
    elif opcao == 6:
        loop = 0
Sqlfuncs("127.0.0.1", "empresas",
         user_pass_and_con[0], user_pass_and_con[1]).desconecta(user_pass_and_con[2])
