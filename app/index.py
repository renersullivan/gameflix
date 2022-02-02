from auth import Iniciar
from menu import Settings


Iniciar.init()
retorno = Settings.escolha_menu()
print(retorno)

while retorno == 459:
    Settings.escolha_menu()
