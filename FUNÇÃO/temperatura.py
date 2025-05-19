print("conversor de temperatura")
print("")

def celsius_fahrenheit(graus):
    n1 = graus  * 1.8 
    fahrenheit = n1 + 32
    return fahrenheit

def celsius_kelvin(kelvin):
    parakelvin = graus + 273
    return parakelvin

def exibir_conversão(graus):
    print("O resultado é", celsius_fahrenheit(graus),"em fahrenheit")
    print("O resultado", celsius_kelvin(graus), "em kelvin")
   

graus = float(input("Digite a temperatura:"))
exibir_conversão(graus)