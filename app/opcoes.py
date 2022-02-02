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
            return
        elif saq <= saldo:
            print(
                '\033[1;32mSAQUE REALIZADO COM SUCESSSO \033[mNO VALOR DE {} REIAS'.format(saq))

    def saircaixa():
        sair = input('''Deseja realmente sair do caixa etronico ? :
        # 1 para sair 
        # 2 para retornar ao menu 
        # 
        # : ''')
        if sair == '1':
            print('OBRIGADO VOLTE SEMPRE  !!!')
        elif sair == '2':
            return 459
