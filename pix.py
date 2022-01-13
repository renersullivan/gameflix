class Pix:

    def pix():

        escolha_pix =input(''' escolha a chave pix:
        # 1 - numero de telefone 
        # 2 - email
        # 3 - CPF 
        # 
        # : ''')
        if escolha_pix == '1':
          
            pix    = input('digite o numero de telefone : ')
            valor1 = input('digite o valor que deseja transferir : ')
            print('voce acabou de transferir {} reais para o numero {}'.format(valor1,pix))

        elif escolha_pix== '2':
          
            email  = input('digite o email que deseja fazer a transferencia : ')
            valor2 = input('digite o valor que deseja transferir : ')
            print('voce acabou de transferir {} reais para o email {}'.format(valor2,email))
        elif escolha_pix =='3':
           
            cpf    = input('digite o CPF   que deseja fazer a transferencia : ')
            valor3 = input('digite o valor que deseja transferir : ')
    