from abc import ABC, abstractmethod


class A(ABC):
    @abstractmethod
    def fala(self, msg):
        ...


class B(A):
    def fala(self, msg):
        print(f'{B.__name__} está falando {msg}')


class C(A):
    def fala(self, msg):
        print(f'{C.__name__} está falando {msg}')


b = B()
c = C()
b.fala('Olá')
c.fala('Cleber')