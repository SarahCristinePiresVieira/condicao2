#Verificação de Credenciais:Dado um login e senha, use o match-case
#para verificar se eles correspondem a uma das seguintes combinações:
#("admin", "admin_pass")
#("user", "user_pass")
#("guest", _)
#Retorne uma mensagem apropriada para cada combinação,
#e uma mensagem de erro se não houver correspondência.


login = str(input('digite seu login:'))
senha = str(input('digite sua senha:'))
match(login, senha):
    case("admin", "admin_pass"):
        print('logado com sucesso!')
    case ("user", "user_pass"):
        print('logado com sucesso!')
    case("guest", _):
        print('logado com sucesso!')
    case _:
        print('login ou senha incorreto')