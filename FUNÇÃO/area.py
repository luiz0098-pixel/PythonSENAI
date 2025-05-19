print("calculador de area")
def circulo(raio) :
    return 3.14 * raio **2
   
def quadrado(numero1) :
    return numero1 * numero1
   
def retangulo(numero1, numero2) :
    return numero1 * numero2
   
def menu_area():
    print("1 circulo")
    print("2 quadrado")
    print("3 retângulo")
   
    opcao = int(input("escolha uma opcao: "))
   
    if opcao == 1:
        raio = float(input("digite o raio do circulo: "))
        print("área do circulo = ",circulo(raio))
       
    elif opcao == 2 :
        lado = float(input("digite o lado do quadrado: "))
        print("área do quadrado = ", quadrado(lado))
       
    elif opcao == 3 :
        base = float(input("digite a base do retangulo: "))
        altura = float(input("digite a altura do retangulo"))
        print("área do retângulo = ", retangulo(base, altura))
menu_area()
