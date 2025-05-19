import random
print("\033[30;42mJogo de adivinhação!\033[m")
print("vamos competir comigo!")
print("o jogo funciona da seguinte maneira: eu vou pensar em um numero de 0 a 100 e voce vai ter")
print("que adivinha! para te ajudar vou falar se o numero é maior ou menor!")
print("tente adivinhar!")
n_computador = random.randint( 0, 100 )
while True:
    num = int(input("escolha um numero:"))
    if num > n_computador:
        print("o numero é menor!")
    elif num < n_computador:
        print("o numero é maior!")
    elif num == n_computador:
        print("voce ganhou!")
        
        print("deseja jogar denovo?")
        print("1 - sim")
        print("2 - não")
        escolha = int(input("digite a sua opção aqui:"))
        if escolha == 1 :
            print("o jogo recomeçou !!")
        else:
            print("o jogo acabou!!")
            break 