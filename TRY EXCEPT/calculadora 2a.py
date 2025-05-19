import inputs

def calculo(n1, n2):
    print("Os resultados são :", adicao(n1,n2) ,"na adição, " , subtracao (n1,n2) ,"na subtração, ", multiplicacao (n1,n2) , "na multiplicação e " ,  divisao (n1,n2) , "na divisão")
 
 
#exercicio 3.1
 
def adicao (n1 , n2):
    conta_soma = n1 + n2
    return conta_soma
 
def subtracao (n1 , n2):
    conta_subtração = n1 - n2
    return conta_subtração
 
def multiplicacao (n1 , n2):
    conta_multiplicação = n1 * n2
    return conta_multiplicação
 
def divisao (n1 , n2):
    conta_divisão = n1 / n2
    return conta_divisão
 
 
#exercicio 3.2
 
def menu_calculadora():
    print("Calculadora")
    print("1) adição")
    print("2) subtração")
    print("3) multiplicação")
    print("4) divisão")
    print("5) Para todas as opções anteriores")
def soma(n1, n2):
    return n1+n2
 
def subtracao(n1, n2):
    return n1-n2
 
def multiplicacao(n1, n2):
    return n1*n2
 
def divisao(n1, n2):
    return n1/n2
 
def todas_opcoes(n1, n2):
    print("o resultado da soma é ", soma(n1, n2))
    print("o resultado da subtração é ", subtracao(n1, n2))
    print("o resultado da multiplicação é ", multiplicacao(n1, n2))
    print("o resultado da divisão é ", divisao(n1, n2))
def calculo(n1, n2, operacao):
    if operacao == 1:
        print("o resultado da soma é",soma(n1, n2))
    elif operacao == 2:
        print("o resultado da subtração é", subtracao(n1, n2))
    elif operacao == 3:
        print("o resultado da multiplicação é", multiplicacao(n1, n2))
    elif operacao == 4:
        print("o resultado da divisão é", divisao(n1, n2))
    elif operacao == 5:
        tudo(n1, n2)
    else:
        print("Erro, Operação não reconhecida")
 
menu_calculadora()
 

operacao = inputs.input_int("digite a sua escolha: ")

n1 = inputs.input_int("Digite o primeiro número: ")

n2 = inputs.input_int("Digite o segundo número: ")
  
