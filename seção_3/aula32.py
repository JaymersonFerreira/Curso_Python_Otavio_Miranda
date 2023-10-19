# try:
#     num = int(input("Digita um número inteiro: "))
    # se num divido por 2 restar 0 execute: print()
#     if num % 2 == 0:
#         print(f"O número: {num} é PAR")
#     elif  num % 3 == 0:
#         print(F"O número {num} é IMPAR")
# except:
#     (print("Não é um número inteiro!"))

# horario = int(input('Inform a hora: '))
# if 0 < horario <= 11:
#     print('Bom Dia!')
# elif 12 < horario <= 17:
#     print('Boa Tarde!')
# elif 18 < horario <= 23:
#     print('Boa Noite')
# else:
#     print("Erro")


nome = input("Digite seu Nome: ")
if 0 < len(nome) <= 4:
    print('Seu nome é curto')
elif 5 < len(nome) <= 6:
    print('Seu nome é normal')
elif len(nome) > 6:
    print('Seu nome é muito grande')

