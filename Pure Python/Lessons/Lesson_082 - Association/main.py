from Classes import Escritor, Caneta, MaquinaDeEscrever

escritor = Escritor('Clebin')
caneta = Caneta('Bic')
maquina = MaquinaDeEscrever()
escritor.ferramenta = maquina
escritor.ferramenta.escrever()

del escritor
print(caneta.marca)
maquina.escrever()
