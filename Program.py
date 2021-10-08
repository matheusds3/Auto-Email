import mysql.connector
from mysql.connector import Error
import win32com.client as win32
import sqlalchemy
import pandas
import datetime
from time import sleep
import tkinter

# Conexão ao banco de dados da empresa


def connect():
    try:
        global con
        con = mysql.connector.connect(
            host='127.0.0.1',
            database='empresas',
            user=f'{usuario}',
            password=f'{senha}'
        )

    except Error as erro:
        print('Erro de Conexão.')


# Consulta ao banco de dados

def consulta(empresa):
    try:
        connect()
        selecionar_banco = '''use empresas'''
        consulta_sql = 'select * from empresas_datas where nome_empresa = ' + '\'' + empresa + '\''
        cursor = con.cursor()
        cursor.execute(selecionar_banco)
        cursor.execute(consulta_sql)
        linhas = cursor.fetchall()

        for linha in linhas:
            print('Id: ', linha [0])
            print('Empresa: ', linha [1])
            print('E-mail: ', linha [3])
            print('Data de Envio: ', linha[2])
    except Error as erro:
        print('Erro ao consultar tabela: {}'.format(erro))
    finally:
        if con.is_connected():
            cursor.close()
            con.close()

# Atualizar banco de dados

def atualizar(declaracao):
    try:
        connect()
        alterar = declaracao
        selecionar_banco = '''use empresas'''
        cursor = con.cursor()
        cursor.execute(selecionar_banco)
        cursor.execute(alterar)
        con.commit() #faz alteração na tabela
        print('Valor Alterado com sucesso.')
    except Error as erro:
        print('Falha ao atualizar dados na tabela: {}'.format(erro))
    finally:
        if con.is_connected():
            cursor.close()
            con.close()

# Cadastrar dados no banco

def cadastrar(inserir_empresa):
    try:
        connect()
        selecionar_banco = '''use empresas'''
        cursor = con.cursor()
        cursor.execute(selecionar_banco)
        cursor.execute(inserir_empresa)
        con.commit()
        consulta_sql = 'select * from empresas_datas where nome_empresa = ' + '\'' + nome_empresa + '\''
        cursor.execute(consulta_sql)
        linhas = cursor.fetchall()

        for linha in linhas:
            print('Id: ', linha[0])
            print('Empresa: ', linha[1])
            print('E-mail: ', linha[3])
            print('Data de Envio: ', linha[2])
        cursor.close()
        if con.is_connected():
            con.close()
            print('Registro inserido com sucesso!')
            print("Conexão finalizada.")
    except Error as erro:
        print('Erro ao cadastrar valores. Possivelmente já existe no banco.')
    finally:
        if con.is_connected():
            cursor.close()
            con.close()

# Deletar do banco de dados

def deletar(deletar_dado):
    try:
        connect()
        selecionar_banco = '''use empresas'''
        cursor = con.cursor()
        cursor.execute(selecionar_banco)
        consulta_sql = 'select * from empresas_datas where id_empresa = ' + '\'' + id + '\''
        cursor.execute(consulta_sql)
        linhas = cursor.fetchall()

        for linha in linhas:
            print('Id: ', linha[0])
            print('Empresa: ', linha[1])
            print('E-mail: ', linha[3])
            print('Data de Envio: ', linha[2])

        apagar = input('Tem certeza que deseja apagar esta\n'
                       'empresa? s = sim/ n = não ')
        if apagar == 's':
            cursor.execute(deletar_dado)
            con.commit()
            cursor.close()
            if con.is_connected():
                con.close()
                print('Registro deletado com sucesso!')
                print("Conexão finalizada.")
        elif apagar == 'n':
            con.close()
            print('Operação Cancelada pelo usuário.')
            print("Conexão finalizada.")
    except Error as erro:
        print('Erro ao deletar valores.')
    finally:
        if con.is_connected():
            cursor.close()
            con.close()

# interface gráfica

tkinter.Tk
















# Início do Programa
ct = 0
while ct == 0:
    try:
        usuario = input('Digite o Usuário: ')
        senha = input('Digite a Senha: ')
        connect()
        sleep(2)
        if con.is_connected():
            print('\nConectado com sucesso.')
            ct = 1
    except:
        print('Falha na conexão com o banco.')


print('\nE-mail automático para empresas.')
print('\nEscolha uma das opções a seguir:\n'
      'cadastrar, consultar, atualizar, deletar\n'
      'enviar?')
ccad = input('')

if ccad == 'cadastrar':

    connect()

    # Criando banco de dados

    cursor = con.cursor()

    criar_banco = '''create database if not exists empresas'''

    selecionar_banco = '''use empresas'''

    criar_tabela = '''create table if not exists empresas_datas (
    id_empresa smallint auto_increment primary key,
    nome_empresa varchar(50) not null,
    data_envio varchar(50) not null,
    email varchar(60) not null
    )'''

    cursor.execute(criar_banco)
    cursor.execute(selecionar_banco)
    cursor.execute(criar_tabela)

    nome_empresa = input('Digite o nome da Empresa: ')
    data_envio = input('Digite a data de envio (dia e mês): ')
    email = input('Digite o email: ')

    dados = '(\'' + nome_empresa + '\',\'' + data_envio + '\',\'' + email + '\''');'

    inserir_empresa = '''insert into empresas_datas (
    nome_empresa, data_envio, email) values ''' + dados

    cadastrar(inserir_empresa)

elif ccad == 'consultar':
    empresa = input('Digite o nome da Empresa: ')
    consulta(empresa)

elif ccad == 'atualizar':
    id = input('Digite o ID da Empresa: ')
    dado = input('Digite o que deseja alterar: ')
    novo_dado = input('Digite o novo valor a ser alterado: ')
    declaracao = '''update empresas_datas
    set ''' + dado + ''' = ''' + '\'' + novo_dado + '\'' + '''
    where id_empresa = ''' + '\'' + id + '\''
    atualizar(declaracao)

elif ccad == 'deletar':
    id = input(('Digite o ID da Empresa a deletar: '))
    deletar_dado = '''delete from empresas_datas where id_empresa = ''' + '\'' + id + '\''
    deletar(deletar_dado)

elif ccad == 'enviar':
# data atual
    data = datetime.datetime.now()
    dia = str(data.day) + str(data.month)
    if len(dia) == 3 and len(str(data.day)) == 1:
        dia = '0' + str(data.day) + str(data.month)
    elif len(dia) == 3 and len(str(data.month)) == 1:
        dia = str(data.day) + '0' + str(data.month)
    elif len(dia) == 2:
        dia = '0' + str(data.day) + '0' +str(data.month)
    else:
        dia = str(data.day) + str(data.month)

# lendo dados da tabela sql

    engine = sqlalchemy.create_engine(f'mysql+pymysql://{usuario}:{senha}@127.0.0.1:3306/empresas')
    dataframe = pandas.read_sql_query(f'select email, id_empresa from empresas_datas where data_envio = {dia}', engine)
    lista = dataframe['email']
    lista_id = dataframe['id_empresa']
    qtd = len(lista)
    print(f'existem {qtd} e-mails para serem enviados hoje.')

# lista de emails a serem enviados

    lista_email = []
    for n in lista:
        lista_email = lista_email + [n]

    lista_ = []
    for n in lista_id:
        lista_ = lista_ + [n]

# interação de envio de e-mails

    n = 0
    while n < qtd:


# criar a integração com o outlook (outlook deve estar funcionando)

        outlook = win32.Dispatch('outlook.application')

# criar um e-mail padrão

        email = outlook.CreateItem(0)
        valores = '20.000'
        arquivo_de_anexo = f'C:\\PythonArchives\\{lista_[n]}.jpeg' # especificar o tipo de anexo
        email.Attachments.Add(arquivo_de_anexo)
        print(arquivo_de_anexo)

# configurar as informações do seu e-mail

        email.To = lista_email[n]
        print(email.To)
        email.Subject = 'email de teste Python'
        email.HTMLBody = f"""
        <p>E-mail automático</p>

        <p>fazendo teste de valores:{valores}R$.</p>

        <p>finalmente o arquivo anexado.</p>
        """
        email.Send()

        sleep(5)

        n = n + 1
        arquivo_de_anexo = None
