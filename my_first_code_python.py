"""
My first code in Python v1.0
11/19/2020

Author: Vinicius Santana

if,else and elif extrutures
"""

print('\nBot: Hello, What is your name? ')
name = (str(input('\nYou: ')))

print(f'\nBot: Hello {name.title()}, How old are you? ')
age = (int(input('\nYou: ')))

if age <= 17:
    print(f'\nBot: Cool {name.title()}, you are {age} years old and you are still a minor!')
    print(f'\nBot: {name.title()}, Which state do you live in? ')
    state = str(input('\nYou: '))
if age >= 18:
    print(f'\nBot: Cool {name.title()}, you are {age} and you are of age!')
    print(f'\nBot: {name.title()}, Which state do you live in? ')
    state = str(input('\nYou: '))

else:
    print(f'\nBot: It should be very good to live in {state.title()}')
    print(f'\nBot: {name.title()}, do you like to study python? [Y/N]')
    answer = str(input('\nYou: '))

if answer != 'Y' and answer != 'N':
    print('\nBot: error, enter a valid command [Y / N]')
elif answer == 'Y':
    print(f'\nBot: Good {name.title()}! I hope you keep studying and improving more and more')
else:
    print(f'\nBot: Ok {name.title()}im sure you will find something else that you like. See you later')
