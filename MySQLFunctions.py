import mysql.connector
from mysql.connector import Error


class Sqlfuncs():

    """conecta ao banco sql"""

    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password

    def conecta(self):
        try:
            global con
            self.con = mysql.connector.connect(
                host=self.host,
                database=" ",
                user=self.user,
                password=self.password
            )
        except Error as erro:
            print('Erro de Conexão.')
        finally:
            print('Conectado com sucesso.')

    def desconecta(self):
        self.con.close()
        print('Conexão Finalizada.')

    # Consulta ao banco de dados

    def consulta(self, table, column_name):

        """consulta dados na tabela sql"""
        cursor = con.cursor()
        try:
            keyword = str(input('Digite o nome que deseja buscar: '))
            selecionar_banco = f'''use {self.database}'''
            consulta_sql = f'select * from {table} where {column_name} = ' + '\'' + keyword + '\''
            cursor.execute(selecionar_banco)
            cursor.execute(consulta_sql)
            linhas = cursor.fetchall()

            for linha in linhas:
                print('Id: ', linha[0])
                print('Empresa: ', linha[1])
                print('E-mail: ', linha[3])
                print('Data de Envio: ', linha[2])
        except Error as erro:
            print('Erro ao consultar tabela: {}'.format(erro))
        finally:
            if con.is_connected():
                cursor.close()

    # Atualizar banco de dados

    def atualizar(self, table, column_id):

        """altera dados na tabela sql"""
        cursor = con.cursor()
        try:
            id_sql = input('Digite o ID que deseja buscar: ')
            dado = input('Digite o que deseja alterar: ')
            novo_dado = input('Digite o novo valor a ser alterado: ')
            sql = f'''update {table}
                        set ''' + dado + ''' = ''' + '\'' + novo_dado + '\'' + f'''
                        where {column_id} = ''' + '\'' + id_sql + '\''

            selecionar_banco = f'''use {self.database}'''
            cursor.execute(selecionar_banco)
            cursor.execute(sql)
            con.commit()
            print('Valor Alterado com sucesso.')
        except Error as erro:
            print('Falha ao atualizar dados na tabela: {}'.format(erro))
        finally:
            if con.is_connected():
                cursor.close()

    # Cadastrar dados no banco

    def cadastrar(self, table, column):

        """cadastrar dados no banco sql"""
        cursor = con.cursor()
        try:
            criar_banco = f'''create database if not exists {self.database}'''
            selecionar_banco = f'''use {self.database}'''
            criar_tabela = f'''create table if not exists {table} (
                        id_empresa smallint auto_increment primary key,
                        nome_empresa varchar(50) not null unique,
                        data_envio varchar(50) not null,
                        email varchar(60) not null
                        )'''

            nome_cadastro = input('Digite o nome a ser cadastrado: ')
            dia_envio = input('Digite dia de envio: ')
            email = input('Digite o email: ')

            dados = '(\'' + nome_cadastro + '\',\'' + dia_envio + '\',\'' + email + '\''');'

            inserir_empresa = f'''insert into {table} (
                        nome_empresa, data_envio, email) values ''' + dados

            cursor.execute(criar_banco)
            cursor.execute(selecionar_banco)
            cursor.execute(criar_tabela)
            cursor.execute(selecionar_banco)
            cursor.execute(inserir_empresa)
            con.commit()

            consulta_sql = f'select * from {table} where {column} = ' + '\'' + nome_cadastro + '\''

            cursor.execute(consulta_sql)
            linhas = cursor.fetchall()

            for linha in linhas:
                print('Id: ', linha[0])
                print('Empresa: ', linha[1])
                print('E-mail: ', linha[3])
                print('Data de Envio: ', linha[2])
            cursor.close()
            if con.is_connected():
                print('Registro inserido com sucesso!')

        except Error as erro:
            print('Erro ao cadastrar valores. Possivelmente já existe no banco.')
        finally:
            if con.is_connected():
                cursor.close()

    # Deletar do banco de dados

    def deletar(self, table, column_id):

        cursor = con.cursor()
        try:
            id_sql = input('Digite o ID da Empresa a deletar: ')
            deletar_dado = f'''delete from {table} where {column_id} = ''' + '\'' + id_sql + '\''
            selecionar_banco = f'''use {self.database}'''
            consulta_sql = f'select * from {table} where {column_id} = ' + '\'' + id_sql + '\''

            cursor.execute(selecionar_banco)
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
                    print('Registro deletado com sucesso!')
            if apagar == 'n':
                deletar_dado = None
                print('Operação Cancelada pelo usuário.')

        except Error as erro:
            print('Erro ao deletar valores.')
        finally:
            if con.is_connected():
                cursor.close()
