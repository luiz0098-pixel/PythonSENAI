print("media aluno")
print("")
nota1 = int(input("coloque a primeira nota do aluno:"))
nota2 = int(input("coloque a segunda nota:"))

if nota1 > 0 and nota1 <= 100 and nota2 > 0 and nota2 <= 100:
    
    adiçao = nota1+nota2
    nota = adiçao/2

    if nota >= 70:
        print(nota, "voce foi aprovado")
    elif nota >= 50 and nota < 70:
        print(nota, "voce esta de recuperação")
    elif nota <50:
        print(nota, "voce esta reprovado")
else:
    print("sua nota é invalida")
