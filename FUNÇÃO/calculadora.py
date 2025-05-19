def menu_calculadora():
    print("escolha uma opção")
    print("1 - soma")
    print("2 - subtração")
    print("3-  multiplicação")
    print("4- divisão")
    menu = input("coloque sua escolha aqui:")
    if menu == "1":
        print(soma(n1, n2))
    elif menu == "2":
        print(subtração(n1, n2))
    elif menu == "3":
        print(multiplicação(n1, n2))
    elif menu == "4":
        print(divisão(n1, n2))
    else:
        print("você digitou o numero errado")
    
def soma (n1 , n2):
        return n1 + n2
def subtração(n1, n2):
        return n1 - n2
def multiplicação(n1, n2):
        return n1 * n2
def divisão (n1, n2):
        return n1/n2
    
def resultado():
    print(soma(n1, n2), "é o resultado da adição!")
    print(subtração(n1, n2), "é o resultado da subtração!")
    print(multiplicação(n1, n2), "é o resultado da multiplicação!")
    print(divisão(n1, n2), "é o resultado da divisão!")
    
n1= float(input("digite um numero:"))
n2 = float(input("digite outro numero:"))

menu_calculadora()

