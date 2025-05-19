print("Índice de Massa Corporal (IMC)")

peso = float(input("informe o seu peso em kg:"))
altura = float(input("informe sua altura em metro:"))

imc = peso/altura**2

if imc <=19:
    print(f'{imc:.2f}, voce esta abaixo do peso')
elif imc >19 and imc <=27:
    print(f'{imc:.2f}imc, voce esta com o peso ideal')
elif imc >27 and imc <=32:
    print(f'{imc:.2f}imc, voce esta acima do peso')
elif imc >32:
    print(f'{imc:.2f}imc, voce esta obeso')
