print("qual o tipo do triangulo")
lado1 = int(input("digite o primeiro lado do triangulo:"))
lado2 = int(input("digite o segundo lado do triangulo:"))
lado3 = int(input("digite o terceiro lado do triangulo:"))

if lado1 == lado2 and lado1 ==lado3 and lado2 ==lado3:
    print("o triangulo é equilatero")
elif lado1 == lado2 and lado1 != lado3 or lado1 == lado3 and lado3!=lado2 or lado2 == lado3 and lado1!=lado3:
    print("o triangulo é isoseres!")
elif lado1 != lado2 and lado1!= lado3 and lado2 != lado3:
    print("o triangulo é escaleno")