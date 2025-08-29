def conta_imc(peso, altura):
    imc_conta = peso / (altura * altura)
    return imc_conta

def classificacao(imc):
    if imc < 18.5:
        print("Abaixo do peso")
    elif imc >= 18.5 and imc <= 24.9:
        print("Peso normal")
    elif imc >= 25 and imc <= 29.9:
        print("Sobrepeso")
    elif imc >= 30:
        print("Obesidade")

peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))
imc = conta_imc(peso, altura)
print("Seu IMC é", round(imc, 2))
classificacao(imc)
