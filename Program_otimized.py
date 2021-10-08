from MySQLFunctions import *
from Emailconfig import *
from tkinter import *
from functools import partial
from tkinter import ttk
# Conexão ao banco de dados

conectar = Conexao('127.0.0.1', 'empresas', 'matheus', '21454867')
enviar = Enviar('127.0.0.1', 'empresas', 'matheus', '21454867')

# dados do banco acessado

table = 'empresas_datas'
column_name = 'nome_empresa'
column_id = 'id_empresa'

# interface do usuário


# Início do Programa
"""
print('\nE-mail automático para empresas.')
print('\nEscolha uma das opções a seguir:\n'
      'cadastrar, consultar, atualizar, deletar\n'
      'enviar?')

"""
consultar = conectar.consulta # (insert table, insert column_name)
atualizar = conectar.atualizar # (insert table, insert column_id)
cadastrar = conectar.cadastrar # (table, column_name)
deletar = conectar.deletar # (table, column_id)


send = enviar.enviar
