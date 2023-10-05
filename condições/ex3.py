#Dias da Semana:
#Escreva uma função que aceite um dia da semana (string) e use o match-case
#para verificar se é um dia útil ("segunda", "terça", etc.) ou fim de semana ("sábado" ou "domingo").
# Retorne uma mensagem apropriada para cada dia.

dia = str(input('digite o dia:'))
match dia:
    case('segunda'|'terça'|'quarta'|'quinta'|'sexta'):
        print(f"{dia} é dia útil")
    case('sabado'|'domingo'):
        print(f"{dia} é final de semana")