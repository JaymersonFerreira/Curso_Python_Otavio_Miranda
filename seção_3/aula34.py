'''
Repetição
while (enquanto)
Executa uma ação enquanto um condição for verdadeira
Loop infinito -> Quando um código não tem fim
'''

condição = True

# while condição:
#     print(1)
#     print(2)
#     print(3)
#     break

while condição:
    nome = input('Qual o seu nome? ')
    print(f'Seu nome é {nome.capitalize()}')

