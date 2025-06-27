#faça uma função que verifica se um numero é positivo ou negarivo e retorne True ou False
def verificar(numero):
    if numero <= 0:
        print("o numero é negativo,", numero)
        return False 
    elif numero >= 1:
        print("o numero é positivo", numero)
        return True        
print("verificar se o numero é positivo ou negativo")
numero = float(input("digite um numero: "))
verificar(numero)