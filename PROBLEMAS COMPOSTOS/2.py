#passo a passo
#passo1 solicite um produto com um preço
#passo2 aplique 5% de desconto

#3
#passo1 dividir 5 por 100  
#passo2: multiplicar pelo valor do produto
#passo3: exibir o valor final e quanto diminui

print("desconto de 5%")
nome = input("digite o nome do produto em reais: ")
preço = int(input("digite o preço do produto: "))
resultado = preço/5
resultado2 =preço-resultado
print( "o novo valor do produto", nome,"é de", resultado2, "reais )
print("e o desconto foi de", resultado, "reais")