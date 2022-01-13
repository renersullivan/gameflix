from ast import Return


class Entrar:

    def login():
        LOGIN_SQL = 'rener'
        SENHA_SQL = '1234'

        login = ''
        senha = ''

        while (login != LOGIN_SQL and senha != SENHA_SQL): 
            login = input('Digite seu login: ')
            senha = input('Digite sua senha: ')
            if login == LOGIN_SQL and senha == SENHA_SQL:
                print('Logou com sucesso')
            else:
                print('Login ou Senha nao encontrado, tente novamente')
                return Entrar.login()
       
    