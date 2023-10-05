#Animais da Fazenda:
#Dado o nome de um animal, use o match-case para verificar se é
#"vaca", "galinha" ou "ovelha". Para qualquer outro animal, retorne "Animal desconhecido".

animal = str(input('digite um animal entre vaca, galinha ou ovelha:'))
match animal:
  case ('vaca'):
    print('digitou vaca')
  case ('galinha'):
    print('digitou galinha')
  case ('verde'):
    print('digitou ovelha')
  case _ :
    print("animal errado!")

