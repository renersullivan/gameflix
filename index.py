from auth import  Entrar
from bootstrap import Init
from menu import Choise
from  extrato import Dinheiro

Init.init()
Entrar.login()

escolhaMenu = Choise.mostrar()

if escolhaMenu == '1':
    Dinheiro.consultaDinheiro()
