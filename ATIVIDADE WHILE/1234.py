while True :
    print("menu")
    print("1- fatorial")
    print("2- quadrado")
    print("3- cubo")
    print("4- tabuada")
    print("0- sair")
    print("")
    escolha = int(input("faça sua escolha:"))
    print("")
    if escolha == 0:
        print("você saiu!")
        break
    
    elif escolha == 1:
        num = int(input("digite um numero:"))
        fatorial = 1
        while (num > 0 ):
            fatorial = fatorial*num
            num = num - 1
            print("o fatorial do numero é:", fatorial )
           
    elif escolha == 2:
        num = int(input("digite um numero para saber seu quadrado: "))
        resultado = num*num
        print("o quadrado é: ", resultado)
       
    elif escolha == 3:
        num = int(input("digite um numero para saber seu cubo: "))
        resultado = num*num*num
        print("o resultado do cubo é", resultado)
       
    elif escolha == 4:
        num = int(input("digite um numero para saber sua tabuada: "))
        print(num, 'X 1 =', num*1)
        print(num, 'X 2 =', num*2)
        print(num, 'X 3 =', num*3)
        print(num, 'X 4 =', num*4)
        print(num, 'X 5 =', num*5)
        print(num, 'X 6 =', num*6)
        print(num, 'X 7 =', num*7)
        print(num, 'X 8 =', num*8)
        print(num, 'X 9 =', num*9)
        print(num, 'X 10 =', num*10)
        
    else:
        print("você digitou o numero errado! tente novamente.")
        
