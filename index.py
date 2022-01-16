from auth import Authentication
from bootstrap import Init
from menu import Choise
from conta import Account
from transferencia.pix import Pix

Init.init()
usuario = Account()
auth = Authentication(usuario)
escolhaMenu = Choise.mostrar()

if escolhaMenu == '1':
    usuario.getSaldo()


auth.logout()