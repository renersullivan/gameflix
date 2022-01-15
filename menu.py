class Choise:

    @staticmethod
    def mostrar() -> object:
        escolhaMenu = input('''
        # 1 - Consultar Saldo
        # 2 - Depositar Dinheiro
        # 3 - Fazer um pix
        # 4 - Sacar dinheiro
        # 5 - Sair do caixa eletronico
    ''')
        return escolhaMenu
