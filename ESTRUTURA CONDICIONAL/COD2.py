#solicite duas notas de um aluno e calcule a media. se a media for maior que ou igual a 70, o aluno esta reprovado. caso contrario, esta aprovado.

nota1 = int(input("digite sua priemira nota:"))
print("")
nota2 = int(input("digite sua segunda nota para saber se foi aprovado:"))

notas1 = nota1+nota2
notas = notas1/2

a_ou_r = ''

if notas >= 70:
    A_ou_R = notas
    print("sua nota foi', notas, 'e você foi aprovado!")
else:
    A_ou_R = notas
    print("sua nota foi", notas, "e você foi reprovado")

