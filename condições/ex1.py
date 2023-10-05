#Classificação Simples de Números:
#Escreva uma função que aceite um número inteiro e use o match-case para verificar se o
#número é 1, 2, ou 3. Para qualquer outro número, retorne "Outro número".

num = int(input('digite um número inteiro entre 1, 2 e 3:'))
match num:
  case 1:
    print('digitou o 1')
  case 2:
    print('digitou o 2')
  case 3:
    print('digitou o 3')
  case _ :
    print("Número errado!")
