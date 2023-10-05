numero = input("Digite um número entre 1 a 3:")
if numero ==1:
    print('amarelo')
elif numero ==2:
    print('azul')
elif numero ==3:
    print('verde')
else:
    print('sem cor')

#-------------------------------ou-----------------------------------------

num = int(input('digite 1 ou 2:'))
match num:
    case 1:
        print('digitou o 1')
    case 2:
        print('digitou o 2')
    case _ :
        print('digitou errado')

#-------------------------------ou-----------------------------------------

login = str(input('digite seu login:'))
senha = str(input('digite sua senha:'))
match(login, senha):
    case('Bruno', '123'):
        print('logado com sucesso!')
    case _ :
        print('login ou senha incorreto')

#-------------------------------ou-----------------------------------------

