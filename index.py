from auth import  Entrar
from bootstrap import Init
from menu import Choise
from  extrato import Dinheiro
from pix import Pix
from sair import Sair


Init.init()
Entrar.login()


escolhaMenu = Choise.mostrar()

if escolhaMenu == '1':
    Dinheiro.consultaDinheiro()
Pix.pix()
Sair.saircaixa()