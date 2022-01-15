import time


class Authentication:

    def __init__(self, conta: object):
        self.conta = conta
        self.login = self.conta.login
        self.senha = self.conta.senha
        Authentication.login(self)

    def login(self):
        LOGIN_SQL = self.login
        SENHA_SQL = self.senha

        login = input('Digite seu login: ')
        senha = input('Digite sua senha: ')
        if login == LOGIN_SQL and senha == SENHA_SQL:
            print('Logou com sucesso')
        else:
            print('Login ou Senha nao encontrado, tente novamente')
            return AuthenticationClass.login()

    def logout(self):
        sair = input('''Deseja realmente sair do caixa etronico ? :

        # 1 para sair 
        # 2 para retornar ao menu 
        # 
        # : ''')
        if sair == '1':
            print('Saindo do caixa...')
            print(self.conta.nome,' deslogou com sucesso!!!')

        elif sair == '2':
            return ()
