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
            if self.con.is_connected:
                print("Conectado")
                return self.con, True
        except Error as erro:
            print("Error")
            return False

    def desconecta(self, con):
        con.close()
        print('Conexão Finalizada.')

    # Consulta ao banco de dados


    def consulta(self, con, table, column_name, keyword):

        """consulta dados na tabela sql"""

        cursor = con.cursor()
        try:
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

    def atualizar(self, con, table, column_id, id_sql, dado, novo_dado):

        """altera dados na tabela sql"""
        cursor = con.cursor()
        try:

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

    def cadastrar(self, con, table, column, nome_cadastro, dia_envio, email):

        """cadastrar dados no banco sql"""
        cursor = con.cursor()
        try:
            criar_banco = f'''create database if not exists empresas'''
            selecionar_banco = f'''use empresas'''
            criar_tabela = f'''create table if not exists {table} (
                        id_empresa smallint auto_increment primary key,
                        nome_empresa varchar(50) not null unique,
                        data_envio varchar(50) not null,
                        email varchar(60) not null
                        )'''
            dados = '(\'' + str(nome_cadastro) + '\',\'' + dia_envio + '\',\'' + str(email) + '\''');'

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

    def deletar(self, con, table, column_id, id_sql):

        cursor = con.cursor()
        try:
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
            """
            apagar = input('Tem certeza que deseja apagar esta\n'
                           'empresa? s = sim/ n = não ')
            if apagar == 's':
                cursor.execute(deletar_dado)
                con.commit()
                cursor.close()
                if con.is_connected():
            """
            cursor.execute(deletar_dado)
            con.commit()
            print('Registro deletado com sucesso!')
            """
            if apagar == 'n':
                deletar_dado = None
                print('Operação Cancelada pelo usuário.')
                """

        except Error as erro:
            print('Erro ao deletar valores.')
        finally:
            if con.is_connected():
                cursor.close()
