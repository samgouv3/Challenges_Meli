import csv
import pandas as pd
import string
from random import choice
from imap_tools import MailBox, AND
import smtplib

#1. Criando função para gerar senhas
def senha_gerada(senha):
    valores = string.ascii_letters + string.digits
    tamanho = 8
    senha = ""
    #print(valores)
    for i in range(tamanho):
        senha += choice(valores)
    return senha

#2. Criando função para gerar id de usuário
def username_gerado(id):
    valores = string.ascii_lowercase
    tamanho = 3
    id = "."
    #print(valores)
    for i in range(tamanho):
        id += choice(valores)
    return id
#3. Lendo arquivo 'users.csv' para gerar credenciais
users=pd.read_csv('users.csv', encoding="UTF-8", sep=";")
nome=users['Nome'].tolist()
sobrenome=users['Sobrenome'].tolist()

#4. Gravando credenciais e senhas no arquivo 'credenciais.csv'
for row in nome:
    with open('credenciais.csv', 'a', newline='')as csvfile:
        nome = users['Nome']
        contas = row+username_gerado(id), senha_gerada('senha')
        my_writer = csv.writer(csvfile, delimiter=';')
        my_writer.writerow(contas)
        print("Contas e Senhas criadas:",contas, "output file: credenciais.csv")
        continue

#5. Leitura do arquivo 'credenciais.csv' gerado.
arquivo =pd.read_csv('credenciais.csv', encoding="UTF-8", sep=";")
contas_criadas=(arquivo[['Username','Password']])
#passw=(arquivo["Password"])
print(contas_criadas)
####################################################################

#6. Conectando ao e-mail e preparando envio
user = "samgouv3@gmail.com"
passw = "senhaparaappgmail"

server_mail=MailBox("imap.gmail.com").login(user,passw)
FROM = 'samgouv3@gmail.com'
#TO = 'matheus.doliveira@mercadolivre.com'
TO = users['Email']
SUBJECT = "Hello!"
TEXT = "This message was sent with Python's smtplib."

#7. Preparando mensagem
mensagem = """\
#From: %s
#To: %s
#Subject: %s
#%s
""" % (FROM, ", ".join(TO), SUBJECT, TEXT)

#8.Enviando Email
server = smtplib.SMTP('imap.gmail.com')
server.sendmail(FROM, TO, mensagem)
server.quit()
