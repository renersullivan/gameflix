from opcoes import Painel


class Settings:

    def escolha_menu():
        escolhaMenu = input('''
        # 1 - Consultar Saldo
        # 2 - Depositar Dinheiro
        # 3 - Fazer um pix
        # 4 - Sacar dinheiro
        # 5 - Sair do caixa eletronico

           ## :''')

        if escolhaMenu == '1':
            return Painel.consultaSaldo()
                      
        elif escolhaMenu == '2':
            Painel.depositarDinheiro()
        elif escolhaMenu == '3':
            Painel.pix()
        elif escolhaMenu == '4':
            Painel.sacarDinheiro()
        elif escolhaMenu == '5':
            return Painel.saircaixa()
