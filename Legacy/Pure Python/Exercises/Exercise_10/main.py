from banco import Banco
from pessoa import Cliente
from conta import ContaCorrente, ContaPoupanca

banco = Banco()

cliente1 = Cliente('Arthur', 16)
cliente2 = Cliente('Cleber', 30)
cliente3 = Cliente('Alfred', 40)

conta1 = ContaPoupanca(1111, 254136, 0)
conta2 = ContaPoupanca(2222, 254137, 0)
conta3 = ContaCorrente(3334, 254138, 0)

cliente1.inserir_conta(conta1)
cliente2.inserir_conta(conta2)
cliente3.inserir_conta(conta3)

banco.inserir_clientes(cliente1)
banco.inserir_conta(conta1)

if banco.autenticar(cliente1):
    cliente1.conta.depositar(40)
    cliente1.conta.sacar(20)
else:
    print('cliente não autenticado')