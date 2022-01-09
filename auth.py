class Auth:

    def login():
        LOGIN_SQL = 'felipe'
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
       
       
    