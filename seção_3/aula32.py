# try:
#     num = int(input("Digita um número inteiro: "))
#     if num % 2 == 0:
#         print(f"O número: {num} é PAR")
#     elif  num % 3 == 0:
#         print(F"O número {num} é IMPAR")
# except:
#     (print("Não é um número inteiro!"))

horario = input('Informe a hora: ')
try:
    horario_int = int(horario)
    if 0 < horario_int <= 11:
        print('Bom Dia!')
    elif 12 < horario_int <= 17:
        print('Boa Tarde!')
    elif 18 < horario_int <= 23:
        print('Boa Noite')
    else:
        print('Não conheço este número')
except:
        print("Digite um número válido!")


nome = input("Digite seu Nome: ")
if 0 < len(nome) <= 4:
    print('Seu nome é curto')
elif 5 < len(nome) <= 6:
    print('Seu nome é normal')
elif len(nome) > 6:
    print('Seu nome é muito grande')

