from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia, conta, saldo):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    def depositar(self, valor: float):
        self.saldo += valor
        self.detalhes()

    @abstractmethod
    def sacar(self, valor):
        ...

    def detalhes(self):
        print(f'Agencia: {self.agencia} \n'
              f'Conta: {self.conta} \n'
              f'Saldo: {self.saldo}')


class ContaPoupanca(Conta):
    def sacar(self, valor):
        if valor > self.saldo:
            print('Sem saldo suficiente')
            return
        self.saldo -= valor
        self.detalhes()


class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo, limite=100):
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def sacar(self, valor):
        if (self.limite + self.saldo) < valor:
            print('Sem saldo suficiente')
            return
        self.saldo -= valor
        self.detalhes()

