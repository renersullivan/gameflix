from auth import Iniciar
from menu import Settings


Iniciar.init()
retorno = Settings.escolha_menu()
print('FORA DO WHILE',retorno)

while retorno == 459:
   retorno = Settings.escolha_menu()
   print('DENTRO DO WHILE:',retorno)