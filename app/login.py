from os import system
from colorama import init, Fore, Back, Style
from getpass import getpass
import stdiomask
from time import sleep


class Login_cadastro:

    init(autoreset=True)


def exibir_menu():
    print(Fore.GREEN + '''          Bem-Vindos ao banco RSA
                    Faça seu login !!
Escolha uma opção:
[1] Cadastrar novo usuario
[2] Fazer login
[3] Sair

''')

    opcao = int(input('Digite uma opção:'))
    return(opcao)


def fazer_login():
    login = input('Nome:')
    senha = stdiomask.getpass(prompt='senha:', mask='#')
    return(login, senha)


def buscar_usuario(login, senha):
    usuarios = []
    try:
        with open('usuarios.txt', 'r+', encoding='utf-8', newline='') as arquivo:
            for linha in arquivo:
                linha = linha.strip(",")
                usuarios.append(linha.split())
                #login, senha = fazer_login()
            for usuario in usuarios:
                nome = usuario[0]
                password = usuario[1]
                if login == nome and senha == password:
                    return True
    except FileNotFoundError:
        return False


while True:

    opcao = exibir_menu()

    if opcao == 1:
        # cadastrar novo usuarios
        login, senha = fazer_login()
        if login == senha:
            print('\033[1;31mSua senha deve ser diferente do login.\033[m')
            senha = getpass(login, senha)
        user = buscar_usuario(login, senha)
        if user == True:
            print(Fore.RED+'Usuario ja existente !!')
            sleep(2)
            # exit()
        else:
            with open('usuarios.txt', 'r+', encoding='utf-8', newline='') as arquivo:
                arquivo.writelines(f'{login} {senha}\n')
            print(Fore.CYAN + 'Cadastro aprovado !!')

            exit()
    elif opcao == 2:
        # fazer o login do usuario
        login, senha = fazer_login()
        user = buscar_usuario(login, senha)
        if user == True:
            print(Fore.CYAN + 'Login realizado com sucesso !!')
            sleep(1)
             

        else:
            print(Fore.RED+'''Voçê deve ter digitado seu nome de usuario
                  ou senha  errado.\n Por favor verifique e escolha uma nova op !!''')
    else:

        print(Fore.LIGHTMAGENTA_EX + 'Good Bay !!')
        break
