import win32com.client as win32
import pandas
import datetime
from time import sleep


# data atual

data = datetime.datetime.now()
dia = str(data.day)
if len(dia) == 1:
    dia = '0' + str(data.day)
else:
    dia = str(data.day)

# lendo dados da tabela sql


class Enviar():

    """Envia e-mails automáticos com anexos para diversos objetos do banco de dados"""

    def __init__(self, host, database, user, password, con):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.con = con

    def enviar(self):

        # lendo dados da tabela sql

        dataframe = pandas.read_sql_query(
            f'select email, id_empresa from empresas_datas where data_envio = {dia}', self.con)
        lista_aux_email = dataframe['email']
        lista_aux_id = dataframe['id_empresa']
        qtd = len(lista_aux_email)
        print(f'existem {qtd} e-mails para serem enviados hoje.')

        # lista de emails a serem enviados

        lista_email = [email for email in lista_aux_email]
        lista_id = [idemp for idemp in lista_aux_id]

        # interação de envio de e-mails

        n = 0
        while n < qtd:

            # criar a integração com o outlook (outlook deve estar funcionando)

            outlook = win32.Dispatch('outlook.application')

            # criar um e-mail padrão

            email = outlook.CreateItem(0)
            valores = '20.000'

            # anexar arquivo (pode ser alterado para o usuario digitar o caminho do arquivo)

            arquivo_de_anexo = f'C:\\PythonArchives\\{lista_id[n]}.pdf'
            email.Attachments.Add(arquivo_de_anexo)

            # configurar as informações do seu e-mail

            email.To = lista_email[n]
            email.Subject = 'email de teste Python'
            email.HTMLBody = f"""
            <p>E-mail automático</p>

            <p>fazendo teste de valores:{valores}R$.</p>

            <p>finalmente o arquivo anexado.</p>
            """
            # email.Send()

            sleep(5)

            n = n + 1
            arquivo_de_anexo = None

        print('E-mails enviados.')
