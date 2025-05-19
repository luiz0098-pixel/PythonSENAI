import random

print("jogo par ou impar")
print("")

while True:
    print("escolha o que quer fazer!")
    print("")
    print("digite 0 para o tuturial do jogo")
    print("digite 1 para jogar")
    print("digite 2 para sair")
    escolha = int(input("digite a sua escolha:"))
    
    if escolha == 0:
        print("1°- escolha se quer par ou impar:")
        print("2°- digite um numero de 0 a 10:")
        print("3°- descubra quem ganhou")
        print("o jogo funciona da seguinte maneira:")
        print("voce e eu escolhemos se queremos par ou impar, depois, escolhemos um numero de 0 a 10 cada um. apos isso, a soma dos numeros é efetuada e o resutado se é par ou impar vai definir quem ganhou!")
    elif escolha ==1 :
        i_p = int(input("digite 1 para escolher impar, e 2 para escolher par. Digite aqui:"))
        n = int(input("digite um numero de 0 a 10:"))
        n2 = random.randint(1, 10)
        soma = n+n2
        print("")
        print("eu escolhi o numero", n2)
        print("voce escolheu o numero", n)
        print("")
        if i_p == 2 and soma % 2 ==0:
            print(soma, "a soma é par, voce ganhou!")
        elif i_p == 2 and soma % 2 ==1:
            print(soma, "a soma é impar, voce perdeu!")
        elif i_p == 1 and soma % 2 ==0:
            print(soma, "a soma é par, voce perdeu!")    
        else:
            print(soma, "a soma é impar, voce ganhou!")
            
    elif escolha ==2:
        print("voce saiu!")
        break 
    
    else:
        print("opção invalida")