print("Conversor de Temperatura")
print("")

def celsius_fahrenheit(graus):
    return graus * 1.8 + 32

def celsius_kelvin(graus):
    return graus + 273.15   # valor mais correto é 273.15, não 273

def exibir_conversao(graus):
    print("O resultado é", celsius_fahrenheit(graus), "°F (Fahrenheit)")
    print("O resultado é", celsius_kelvin(graus), "K (Kelvin)")

graus = float(input("Digite a temperatura em °C: "))
exibir_conversao(graus)
