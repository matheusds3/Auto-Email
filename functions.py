import mysql.connector
from mysql.connector import Error
from tkinter import messagebox
import pymysql.cursors

class Sqlfuncs():

    """conecta ao banco sql"""

    def __init__(self):
        pass

    def conecta(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        try:
            global con
            self.con = pymysql.connect(
                host=self.host,
                database="empresas",
                user=self.user,
                password=self.password
            )
            #if self.con.is_connected:
            return self.con, True
        except Error as erro:
            messagebox.showinfo("Erro", "Dados Incorretos!")
            return None, False

    def desconecta(self, con):
        con.close()
        messagebox.showinfo("", "Conexão Finalizada.")

    # Consulta ao banco de dados

    def consulta(self, con, table, column_name, keyword):

        """consulta dados na tabela sql"""

        cursor = con.cursor()
        if keyword == "":
            messagebox.showinfo("", "Insira o nome!")
        else:
            try:
                selecionar_banco = '''use empresas'''
                consulta_sql = f'select * from {table} where {column_name} = ' + '\'' + keyword + '\''
                cursor.execute(selecionar_banco)
                cursor.execute(consulta_sql)
                linhas = cursor.fetchall()

                for linha in linhas:
                    self.id = linha[0]
                    self.empresa = linha[1]
                    self.email = linha[3]
                    self.envio = linha[2]


                messagebox.showinfo("Consulta", "Dados:\n"
                                                f"Id: {self.id}\n"
                                                f"Empresa: {self.empresa}\n"
                                                f"E-mail: {self.email}\n"
                                                f"Data de Envio: {self.envio}")
            except Error as erro:
                messagebox.showinfo("Erro", "Erro ao consultar {}".format(erro))
            finally:
                #if con.is_connected():
                cursor.close()

    # Atualizar banco de dados

    def atualizar(self, con, table, column_id, id_sql, dado, novo_dado):

        """altera dados na tabela sql"""
        cursor = con.cursor()
        try:

            sql = f'''update {table}
                        set ''' + dado + ''' = ''' + '\'' + novo_dado + '\'' + f'''
                        where {column_id} = ''' + '\'' + id_sql + '\''

            selecionar_banco = '''use empresas'''
            cursor.execute(selecionar_banco)
            cursor.execute(sql)
            con.commit()
            messagebox.showinfo("Atualizado", "Registro Atualizado\n"
                                              " com Sucesso!")
        except Error as erro:
            messagebox.showinfo("Erro", "Falha ao atualizar dados na tabela:\n"
                                        " {}".format(erro))

        finally:
            #if con.is_connected():
            cursor.close()

    # Cadastrar dados no banco

    def cadastrar(self, con, table, column, nome_cadastro, dia_envio, email):

        """cadastrar dados no banco sql"""
        cursor = con.cursor()
        if nome_cadastro == "" or dia_envio == "" or email == "":
            messagebox.showinfo("", "Dados Incompletos.")
            pass
        else:
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
                    self.id = linha[0]
                    self.empresa = linha[1]
                    self.email = linha[3]
                    self.envio = linha[2]


                cursor.close()
               # if con.is_connected():
                messagebox.showinfo("Registrado", "Registro Inserido com Sucesso!\n"
                                                  f"Id: {self.id}\n"
                                                  f"Empresa: {self.empresa}\n"
                                                  f"E-mail: {self.email}\n"
                                                  f"Data de Envio: {self.envio}")

                return linhas

            except Error as erro:
                messagebox.showinfo("Erro", "Falha ao inserir valores:\n"
                                            "Já existe um registro\n"
                                            " com mesmo nome!")

            finally:
               # if con.is_connected():
                 cursor.close()

    # Deletar do banco de dados

    def deletar(self, con, table, column_id, id_sql):

        cursor = con.cursor()
        if id_sql == "":
            messagebox.showinfo("Erro", "Insira o ID!")
        else:
            try:
                deletar_dado = f'''delete from {table} where {column_id} = ''' + '\'' + id_sql + '\''
                selecionar_banco = f'''use empresas'''
                consulta_sql = f'select * from {table} where {column_id} = ' + '\'' + id_sql + '\''

                cursor.execute(selecionar_banco)
                cursor.execute(consulta_sql)
                linhas = cursor.fetchall()

                for linha in linhas:
                    self.id = linha[0]
                    self.empresa = linha[1]
                    self.email = linha[3]
                    self.envio = linha[2]
                #if con.is_connected():
                messagebox.showinfo("", "Registro Deletado com Sucesso!\n"
                                        f"Id: {self.id}\n"
                                        f"Empresa: {self.empresa}\n"
                                        f"E-mail: {self.email}\n"
                                        f"Data de Envio: {self.envio}")
                cursor.execute(deletar_dado)
                con.commit()
            except Error as erro:
                messagebox.showinfo("Erro", "Erro ao deletar dado.")
            finally:
                #if con.is_connected():
                cursor.close()
