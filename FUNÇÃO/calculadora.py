def soma(n1, n2):
    return n1 + n2

def subtracao(n1, n2):   
    return n1 - n2

def multiplicacao(n1, n2):   
    return n1 * n2

def divisao(n1, n2):   
    if n2 == 0:
        return "Erro: divisão por zero!"
    return n1 / n2

def menu_calculadora(n1, n2):
    print("Escolha uma opção:")
    print("1 - soma")
    print("2 - subtração")
    print("3 - multiplicação")
    print("4 - divisão")
    
    menu = input("Coloque sua escolha aqui: ")
    if menu == "1":
        print(soma(n1, n2))
    elif menu == "2":
        print(subtracao(n1, n2))
    elif menu == "3":
        print(multiplicacao(n1, n2))
    elif menu == "4":
        print(divisao(n1, n2))
    else:
        print("Você digitou um número errado.")

def resultado(n1, n2):
    print(soma(n1, n2), "é o resultado da adição!")
    print(subtracao(n1, n2), "é o resultado da subtração!")
    print(multiplicacao(n1, n2), "é o resultado da multiplicação!")
    print(divisao(n1, n2), "é o resultado da divisão!")

# programa principal
n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))

menu_calculadora(n1, n2)
