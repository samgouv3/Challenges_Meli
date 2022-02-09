import pandas as pd
import mysql.connector
from imap_tools import MailBox, AND

#1. Conectando ao e-mail e pesquisando
user = "samgouv3@gmail.com"
passw = "bsadjpljsprekkyg"
meu_email=MailBox("imap.gmail.com").login(user,passw)
lista_emails= meu_email.fetch(AND(from_="support@grindinggear.com",text="DevOps"))
#lista_emails= meu_email.fetch(AND(text="DevOps"))
for email in lista_emails:
    #print(len(list(lista_emails)))
    print(email.subject)

#2. Conectando ao banco de dados e criando tabela
try:
    con = mysql.connector.connect(host='localhost',user='root',passwd='',database='Challenge2')
    criar_tabela_sql="""CREATE TABLE tbl_email(datamail DATE,origem VARCHAR(20),assunto VARCHAR(20))"""
    cursor = con.cursor()
    cursor.execute(criar_tabela_sql)
    print("Tabela criada com sucesso")

#3. Criado retorno de mensagem de erro
except mysql.connector.Error as erro:
    print("Falha ao criar tabela no Mysql: {}".format(erro))

#4. Desconectando do banco de dados
finally:
    if(con.is_connected()):
        cursor.close()
        con.close()
        print("Conexão finalizada")