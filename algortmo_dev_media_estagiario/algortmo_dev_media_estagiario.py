"""
Algoritmo desafio dev media estagiário
Author: Vinicius Santana

# Enunciado:

Faça um algoritmo para ler um número que é um código de usuário.

Caso este código seja diferente de um código armazenado internamente no algoritmo (igual a 1234) deve ser apresentada a
mensagem "Usuário inválido!" e o sistema será encerrado.

Caso o código seja correto, deve ser lido outro valor que é a senha.

Se a senha estiver correta (a certa é 9999), deve ser exibida a mensagem "Acesso permitido".

Se a senha estiver incorreta deve ser exibida a mensagem "Senha incorreta", e também uma mensagem com as seguintes
opções:

1 - tentar novamente
0 - encerrar sistema

# Code:
"""

while True:
    usuario = 1234
    senha = 9999
    resp = 1 and 0

    usuario = int(input("Digite o número de usuário: "))

    if usuario == 1234:
        senha = int(input("Usuario correto, entre com a senha: "))
    else:
        print('\nUsuario Inválido!')
        break
    if senha == 9999:
        print("Acesso permitido!")
    elif senha != 9999:
        print("\nSenha incorreta!\n")
        resp = int(input("Escolha uma opção: \n1 - tentar novamente\n0 - Sair\n\nResposta: "))
    while resp != 1 and resp != 0:
        print("Opção errada, tente novamente")
        resp = int(input("Escolha uma opção: \n1 - tentar novamente\n0 - Sair\nResposta: "))
    if resp == 1:
        continue
    else:
        break





