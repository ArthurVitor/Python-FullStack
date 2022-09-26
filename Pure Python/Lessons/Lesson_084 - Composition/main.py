from classes import Cliente

cliente1 = Cliente('Arthur', 16)
print(cliente1.nome)
cliente1.insere_endereco('Belo Horizonte', 'MG')
cliente1.insere_endereco('Joao Pessoa', 'PB')
cliente1.lista_enderecos()
print()

cliente2 = Cliente('Cleber', 25)
print(cliente2.nome)
cliente2.insere_endereco('Joao Pessoa', 'PB')
cliente2.insere_endereco('Gramado', 'RS')
cliente2.lista_enderecos()
print()

cliente3 = Cliente('Alfred', 54)
print(cliente3.nome)
cliente3.insere_endereco('Sao Paulo', 'SP')
cliente2.lista_enderecos()
