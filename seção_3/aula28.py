nome = ''
idade = 0
if nome == '':
    nome = input('Digite seu nome: ')

if idade == 0:
    idade = input('Digite sua idade: ')
    if idade == '':
        idade = 0

idade_int = int(idade)
if nome and idade:
    print(f'Seu nome ne {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')
else:
    print('Desculpe, você deixou campos vazios')