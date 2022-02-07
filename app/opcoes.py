from random import randint


class Painel:
    saldo = randint(100, 2000)

    def depositarDinheiro():
        saldo = randint(100, 2000)
        print('Seu saldo eh de R$', saldo, 'reias')
        escolha_dep = int(input('Deseja depositar quanto?'))
        if escolha_dep > saldo:
            print('\033[1;31m ****** SALDO INSULFICIENTE !! ******\033[m')
            return

        elif escolha_dep <= saldo:
            print(escolha_dep, ' depositado com sucesso!!!')
            return
        else:
            print('Valor inválido digite um valor numerico !!')
            return Painel.depositarDinheiro()

    def consultaSaldo():
        saldo = randint(100, 2000)
        print('seu saldo é de R$', saldo, 'reais...')
        return Painel.saircaixa()

    def senhas():
        pws = input('Digite sua senha para confirmar a transacao : ')
        confir = input('Digite novamente sua senha para confirmar :  ')
        if pws != confir:
            print(
                '\033[1;31m!!!!!!! senha incorreta digite novamente !!!!!!!\033[m')
            return Painel.senhas()
        else:
            print('\033[1;32m!!!! transferencia feita com sucesso !!!\033[m')
            return

    def sacarDinheiro():
        saldo = randint(100, 2000)
        print('*** Saldo de R$', saldo, 'reais *** ')
        saq = int(input('Digite o valor que deseja sacar :'))
        if saq > saldo:
            print('\033[1;31m ****** SALDO INSULFICIENTE !! ******\033[m')
            return Painel.saircaixa()
        elif saq <= saldo:
            print(
                '\033[1;32mSAQUE REALIZADO COM SUCESSSO \033[mNO VALOR DE {} REIAS'.format(saq))
            return Painel.saircaixa()

    def saircaixa():
        sair = input('''Gostaria de fazer o que agora ? :
        # 1 para sair 
        # 2 para retornar ao menu 
        # 
        # : ''')
        if sair == '1':
            print('OBRIGADO VOLTE SEMPRE  !!!')
            return 9999
        elif sair == '2':
            return 459

    def pix():
        transferencia = input('''escolha chave pix  para fazer a transferencia 
        # 1 para email :
        # 2 para numero de celular :
        # 3 para CPF 
        #---> :''')
        if transferencia == '1':
            email = input('''Digite o email para qual deseja relaizar o PIX:
             # -> :''')
            valor = input('Agora digite o valor que deseja transferir :')
            print(
                f'O valor {valor} foi depositado corretamente no email {email}')
            return Painel.saircaixa()

        elif transferencia == '2':
            cel = input('''Digite o numero de celular para qual deseja relaizar o PIX:
             # -> :''')
            valor = input('Agora digite o valor que deseja transferir :')
            print(
                f'O valor {valor} foi depositado corretamente na chave pix : {cel}')
            return Painel.saircaixa()

        elif transferencia == '3':
            cpf = input('''Digite o CPF para qual deseja relaizar o PIX:
             # -> :''')
            valor = input('Agora digite o valor que deseja transferir :')
            print(
                f'O valor {valor} foi depositado corretamente no CPF : {cpf}')
            return Painel.saircaixa()
        else:
            print(
                '\33[1;31mA opção escolhida nao eh valida tente novamente !!\33[m')
            return Painel.pix()
