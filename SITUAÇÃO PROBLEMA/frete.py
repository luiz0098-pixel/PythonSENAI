#Crie uma função que calcula o valor do frete da segunte forma: valor = (peso x 0.5) + (distancia x 0.1) + taxa_fixa
def calcular(peso, distancia, taxa_fixa):
    valor = (peso * 0.5) + (distancia *0.1) + taxa_fixa
    print("o valor do frete sera de", valor, "reais")
peso = int(input("qual o peso do frete? coloque aqui:"))
distancia = int(input("qual a distancia que vai ser percorrida? coloque aqui:"))
taxa_fixa = int(input("qual a taxa fixa? coloque aqui:"))
calcular(peso, distancia, taxa_fixa)