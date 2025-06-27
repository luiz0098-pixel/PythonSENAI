# a temperatura ideal para a qualidade do ar é entre 20°c e 22°c no inverno e 23°c e 26°c no verão. a umidade ideal para a saude humana deve estar
# entre 40% e 55% no inverno e 40% e 65% no verão.
# faça uma função que verifica a qualidade do ar com base nesses dados
def verificar(temperatura, umidade, escolha):
    if escolha == "inverno":
        if temperatura >= 20 and temperatura <= 22:
            if umidade >= 40 and umidade <= 55:
                print("a qualidade do ar esta ideal para o inverno") 
            else:
                print("a qualidade do ar esta inadequada")
    elif escolha == "verao":
        if temperatura >= 23 and temperatura <= 26:
            if umidade >= 56 and umidade <= 65:
                print("a qualidade do ar esta inadequada para o verao")
            else:
                print("a qualidade do ar esta inadequada")
escolha = str(input("coloque a estação inverno o verao:"))
temperatura = int(input("digite a temperatura:"))
umidade = int(input("agora digite a umidade"))
verificar(temperatura, umidade, escolha)

    
