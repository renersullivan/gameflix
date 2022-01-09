#Primeira coisa pra se fazer um software é organizar quais as funcões dele.
#Vamos mapear o que um software de caixa eletronico teria, ok?
################## 
# A) Fazer login usando Agencia e Conta - Feito
# B) Gerar um saldo randomico - Feito
# c) Mostrar um menu contendo as seguintes ações - Feito
# 1 - Consultar Saldo - Feito
# 2 - Depositar Dinheiro - Feito
# 3 - Fazer um pix - feito
# 4 - Sacar dinheiro - feito 
# 5 - Sair do caixa eletronico - feito

import random 
import time

saldo =random.randint(100,3000)

#Declarando
def init():
    print('=='* 12)
    print('** BANCO R.Sullivan **')
    print('=='* 12)
  

#Declarando
def login():
    nome    =input('Qual seu nome : ')
    agencia =input('informe o numero da agencia : ') 
    contas  =input('Digite o numero da sua conta sem digito : ') 
    time.sleep(2)
    print('\033[1;32m!!  LOGADO COM SUCESSO  !!\033[m')


def menu():
   escolhaMenu = input('''
    # 1 - Consultar Saldo
    # 2 - Depositar Dinheiro
    # 3 - Fazer um pix
    # 4 - Sacar dinheiro
    # 5 - Sair do caixa eletronico
   ''')
   if escolhaMenu == '1':
       consultaSaldo()

   elif escolhaMenu == '2':
        depositarDinheiro()
   elif escolhaMenu == '3':
        pix()
   elif escolhaMenu == '4':
        sacarDinheiro()
   elif escolhaMenu == '5':
       saircaixa()

def depositarDinheiro():
    print('Seu saldo eh de R$',saldo,'reias')
    escolha_dep = int(input('Deseja depositar quanto?'))
    if escolha_dep > saldo :
        print('\033[1;31m ****** SALDO INSULFICIENTE !! ******\033[m')
        return menu()
    elif escolha_dep <= saldo:
        print(escolha_dep, ' depositado com sucesso!!!')
        return menu()

def consultaSaldo():
    print('seu saldo é de R$', saldo,'reais...')
    return menu()

def pix():

    escolha_pix =input(''' escolha a chave pix:
    # 1 - numero de telefone 
    # 2 - email
    # 3 - CPF 
    # 
    # : ''')
    if escolha_pix == '1':
      print('*** Saldo de R$',saldo,'reais *** ')
      pix    = input('digite o numero de telefone : ')
      valor1 = input('digite o valor que deseja transferir : ')
      print('voce acabou de transferir {} reais para o numero {}'.format(valor1,pix))

    elif escolha_pix== '2':
        print('*** Saldo de R$',saldo,'reais *** ')
        email  = input('digite o email que deseja fazer a transferencia : ')
        valor2 = input('digite o valor que deseja transferir : ')
        print('voce acabou de transferir {} reais para o email {}'.format(valor2,email))
    elif escolha_pix =='3':
        print('*** Saldo de R$',saldo,'reais *** ')
        cpf    = input('digite o CPF   que deseja fazer a transferencia : ')
        valor3 = input('digite o valor que deseja transferir : ')
   
def senhas():
    pws     = input('Digite sua senha para confirmar a transacao : ')
    confir  = input('Digite novamente sua senha para confirmar :  ')
    if pws!= confir:
        print('\033[1;31m!!!!!!! senha incorreta digite novamente !!!!!!!\033[m')
        return senhas()
    else:
        print('\033[1;32m!!!! transferencia feita com sucesso !!!\033[m') 

        return menu()

def sacarDinheiro():
    print('*** Saldo de R$',saldo,'reais *** ')
    saq = int(input('Digite o valor que deseja sacar :'))
    if saq > saldo :
        print('\033[1;31m ****** SALDO INSULFICIENTE !! ******\033[m')
        return menu()
    elif saq <= saldo :
       print('\033[1;32mSAQUE REALIZADO COM SUCESSSO \033[mNO VALOR DE {} REIAS'.format(saq))

def saircaixa():
    sair = input('''Deseja realmente sair do caixa etronico ? :

    # 1 para sair 
    # 2 para retornar ao menu 
    # 
    # : ''')
    if sair == '1':
        print('OBRIGADO VOLTE SEMPRE  !!!')
    elif sair == '2':
        return menu()
        
#Executar
init()

#Executar
login()

#Executar
menu()

senhas()

