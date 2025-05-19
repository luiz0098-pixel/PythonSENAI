#descubra o dia da semana 

print("digite um numero para saber que dia da semana é hoje!!")
print("")
dia = int(input("digite um número de 1 a 7:"))

if dia==1:
    print("hoje é domingo")
    
elif dia==2:
    print("hoje é segunda-feira")
    
elif dia==3:
    print("hoje é terça-feira")
    
elif dia==4:
    print("hoje é quarta-feira")
    
elif dia==5:
    print('hoje é quinta-feira')

elif dia==6:
    print("hoje é sexta!")
    
elif dia==7:
    print("hoje é sábado!")
else:
    print("dia não reconhecido, por favor verifique se o número está entre 1 e 7")