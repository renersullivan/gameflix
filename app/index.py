from auth import Iniciar
from menu import Settings
from login import Login_cadastro

Iniciar.init()

Login_cadastro.exibir_menu()

retorno = Settings.escolha_menu()
print('FORA DO WHILE',retorno)

while retorno == 459:
   retorno = Settings.escolha_menu()
   print('DENTRO DO WHILE:',retorno)