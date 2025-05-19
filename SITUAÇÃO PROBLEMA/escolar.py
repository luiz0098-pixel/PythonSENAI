import inputs


while True:
    print("incrições para o evento escolar")
    print("")
    print("menu de opções")
    print("1 - cadastrar um nome")
    print("2 - exibir o total de inscritos")
    print("3 - exibir a lista de nomes em ordem alfabética")
    print("4 - permitir a consulta de um nome")
    print("5 - sair")
    print("")
    opcao = inputs.input_int(("Digite sua escolha"))
    print("")
    if opcao == 1:
        nome = inputs.input_int("digite o nome que quer cadastrar")
        if nome in nomes:
            print("nome cadastrado")
        else:
            nomes.append(nome)
            print("nome cadastrado com sucesso")
    elif opcao == 2:
        print("o total de inscritos foram", len(nomes))
    elif opcao == 3:
        for nome in nomes:
            print(nome)
    elif opcao == 4:
        nome = inputs.input_int("digite seu nome que quer consultar")
        if nome in nomes:
            vari = inputs.input_int("nome encontrado, você deseja remover da lista? s/n ")
            if vari == "s":
                nomes.remove(nome)
                print("nome removido")
            elif vari == "n":
                print("o nome ainda permanece na lista")
        else:
            vari1 = inputs.input_int("nome não encontrado, deseja adiciona-lo? s/n")
            if vari1 == "s":
                nomes.append(nome)
                print("o nome foi adicionado à lista")
            elif  vari1 == "n":
                print("ok")
            else:
                print("opção inesistente")
    elif opcao == 5:
        print("você saiu")
        break
    else:
        print("opção inexistente")