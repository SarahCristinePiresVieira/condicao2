#Identificando Cores:
#Dado um nome de cor (string), use o match-case para verificar
#se é "vermelho", "azul" ou "verde". Para qualquer outra cor, retorne "Cor desconhecida".

cor = str(input('digite entre vermelho, azul e verde:'))
match cor:
  case ('vermelho'):
    print('digitou vermelho')
  case ('azul'):
    print('digitou azul')
  case ('verde'):
    print('digitou verde')
  case _ :
    print("cor errada!")
