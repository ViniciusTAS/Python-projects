"""
Titulo: Calculo de média v1.0
Author: Vinicius Santana
data: 24/11/2020
"""
while True:
    print("------------------------------------")
    print("\033[1;34m"+"        Calculo de média            " + "\033[0;0m") #Caracteres ANSI para dar uma cor ao título
    print("------------------------------------")

    n1 = float(input("Digite a tua 1ª nota: "))
    n2 = float(input("Digite a tua 2ª nota: "))
    n3 = float(input("Digite a tua 3ª nota: "))
    print("------------------------------------")

    resultado = (n1 + n2 + n3) / 3
    resp = ""

    if resultado >= 7:
        print(f"A média final é: {resultado:.2f}")
        print("------------------------------------")
        print("Situação é:" "\033[32m" + " Aprovado!" + "\033[0;0m" ) #Caracteres ANSI para dar uma cor ao resultado
        print("------------------------------------")                 #Verde para aprovado e vermelho para reprovado
        resp = input("Deseja continuar? [s/n]")

    else:
        print(f"A média final é: {resultado:.2f}")
        print("------------------------------------")
        print("Situação é: " "\033[31m" + "Reprovado!" + "\033[0;0m'")
        print("------------------------------------")
        resp = input("Deseja continuar? [s/n]")

    if resp == "n":
        break
    else:
        continue

