from datetime import datetime

def hora_funcao(nome):
    hora = datetime.now().hour


    if hora >= 0 and hora <= 5:
        print("boa madrugada", nome)
    
    elif hora > 5 and hora <= 12:
        print("bom dia", nome)
    
    elif hora > 12 and hora <= 19:
        print("boa tarde", nome)
    
    elif hora > 19 and hora <= 24:
        print("boa noite", nome)
    
nome = input("qual o seu nome?:")
hora_funcao(nome)