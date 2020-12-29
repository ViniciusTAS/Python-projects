"""
My first code in Python v1.0
11/19/2020

Author: Vinicius Santana

if,else and elif extrutures
"""

My first code in Python v1.0
11/19/2020

Author: Vinicius Santana

if,else and elif extrutures
"""

print('\nBot: Olá, Qual é o seu nome? ')
name = (str(input('\nVocê: ')))

print(f'\nBot: Olá {name.title()}, quantos anos tem? ')
idade = (int(input('\nVocê: ')))

if idade <= 17:
    print(f'\nBot: Legal {name.title()}, você tem {idade} anos e ainda é menor de idade!')
    
if idade >= 18:
    print(f'\nBot: Legal {name.title()}, você tem {idade} anos e já é maior de idade!')
    
if idade <= 17 or idade >= 18:
    print(f'\nBot: {name.title()}, Qual estado você mora? ')
    estado = (input('\nVocê: '))
    print(f'\nBot: Deve ser muito bom morar em {estado.title()}')
    
    while True:
        print(f'\nBot: {name.title()}, você gosta de estudar python? [Y/N]')
        resp = str(input('\nVocê: '))
        
        if resp == 'Y':
            print(f'\nBot: Boa {name}, continue estudando e melhorando cada vez mais ')
            break
            
        elif resp == "N":
            print(f'\nBot: É uma pena {name}, mas tenho certeza que irá se encontrar em alguma outra linguagem.')
            print('\nBot: Até logo.')
            break
            
        else:
            if resp != 'Y' and resp != 'N':
                print('\nBot: Erro! comando inválido, digite novamente')
