from displayclient import *
from Emailconfig import *

# Programa Para Envio de E-mails Automáticos a Partir de um Banco de Dados MySQL

tela = Tk()

tela1 = Display(tela)
con = tela1.retorna()

loop = 1
while loop != 0:
    tela2 = Display2(tela)
    opcao = tela2.retornou()

    if opcao == 1:
        DisplayCadastrar(tela, con)
        loop = 1
    elif opcao == 2:
        DisplayAtualizar(tela, con)
        loop = 1
    elif opcao == 3:
        DisplayConsultar(tela, con)
        loop = 1
    elif opcao == 4:
        DisplayDeletar(tela, con)
        loop = 1
    elif opcao == 5:
        Enviar(con).enviar()
        loop = 1
    elif opcao == 6:
        loop = 0
Sqlfuncs().desconecta(con)
