import random as rand


class Account:

    def __init__(self,nome = 'Felipe',idade = '22',login = 'rener',senha = '123',telefone = '12343142',cc = '123',ag = '123'):
        self.nome = nome
        self.login = login
        self.senha = senha
        self.idade = idade
        self.telefone = telefone
        self.cc = cc
        self.ag = ag
        self.saldo = saldo = rand.randint(10, 9000)

    def setNome(self,nome):
        self.nome = nome

    def getNome(self):
        return self.nome

    def setAgencia(self,ag):
        self.ag = ag

    def getAgencia(self,ag):
        return self.ag

    def setContaCorrente(self,cc):
        self.cc = cc

    def getContaCorrente(self):
        return self.cc

    def getSaldo(self):
        print(self.saldo)
        return self.saldo
