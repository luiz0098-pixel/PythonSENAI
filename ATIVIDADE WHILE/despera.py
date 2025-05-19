valor_atual = 0
num_despesas = 0

while True:
    print("valor das despesas")
    print("escolha uma opção:")
    print("0- sair")
    print("1- adicionar valor da despesa")
    print("2- mostar a quantidade e o valor total das despesas")
    menu = int(input("coloque sua escolha aqui:"))
    
    if menu == 0:
            print("voce saiu!")
            break
    elif menu == 1:
         adicionar = int(input("coloque o valor das despesas:"))
         print("voce adicionou", adicionar, "reais nas suas despesas")
         
         num_despesas += 1
         valor_atual = adicionar + valor_atual
         
    elif menu == 2:
        print("voce tem um total de", num_despesas, "despesas que somam", valor_atual, "reais de despesas")
    else:
        print("ERROOO!!! opção invalida")
        
    
    
    
        

    
    