#menor ou maior de idade

print("saiba qual é sua idade, e se você é maior ou menor de idade")
print("")
ano = int(input("digite o seu ano de nascimento:"))

idade = 2025-ano


if idade >= 18:
    print("você tem", idade, "anos, e você é maior de idade")
else:
    print('você tem', idade, 'anos e você é menor de idade')