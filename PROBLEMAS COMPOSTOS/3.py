#construa um programa que calcule: quanto custa encher o tanque de um carro que tem 50 litros de capacidade,esta com 20 litros de combustivel atualmente e o custo do combustivel é de 5,80 por litro

#1 quanto custa encher o tanque do carro
#2 capacidade de combustivel do carro em litros, quantos litros o carro ja tem e o valor do litro do combustivel em reais
#3 passo1- subtrair a capacidade total pelo tanque atual
#4 passo2- multiplicar o resultado da subtração pelo preço do combustivel
#4 passo3- exibir o custo em reais

print("tanque do carro atividade 1")
capacidade = 50-20
multiplicar = capacidade*5.80
print("o custo total é de:" , multiplicar, "reais")

print("                        ")
print("                        ")
print("                        ")
#atividade2
print("tanque do carro atividade 2")
capacidade = int(input("digite a capacidade do tanque:"))
tanque = int(input("ja tem gasolina no tanque? coloque o quanto ja tem:"))
valor = float(input("quanto esta o litro da gasolisa?"))
subtracao = capacidade-tanque
multiplicar = tanque*valor
print("o custo total é de:", multiplicar, "reais")
