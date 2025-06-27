alunos = []
def calcular_media (n1, n2, n3):
     return  (n1 + n2 + n3) / 3


def verificar_situação(media): 
    for i in alunos:
        if media >= 7:
            p1  = "Aprovado"
            return p1
        elif media >= 5 and media <= 6.9:
            p1 =  "reculperação"
            return p1
        elif media < 5:
            p1 = "Reprovado"
            return p1
        else:
            print("sua nota é invalida")
        

def cadastro_aluno():  
    aluno1 = {
        "nome": input("Aluno: "),
        "nota1": int(input("nota1: ")),
        "nota2": int(input("nota2: ")),
        "nota3": int(input("nota3: "))
}
    
    alunos.append(aluno1)
    
    for i in alunos:
        media = calcular_media(i["nota1"],i["nota2"],i["nota3"])
        i["media"] = media
        
    return aluno1
    
def exibir_aluno(alunos): 
    for i in alunos:
        print(f"{i['nome']}: {i['media']}")
        
        
while True:
    print("sistema de notas de alunos")
    print("menu de opções")
    print("[1] - cadastrar nome e a nota de um aluno")
    print("[2] - alunos cadastrados e media")
    print("[3]- relatorio")
    print("[4]- sair")
    
    escolha = input("Escolha uma opção: ")
    
    if escolha == "1": 
         cadastro_aluno()
         
    elif escolha == "2": 
        exibir_aluno(alunos)
        
    elif escolha == "3": 
        for i in alunos:
            situa2 = verificar_situação(i["media"])
            i["situacao"] = situa2
            print(f"{i['nome']}: {i['situacao']}")
        
        
    elif escolha == "4": 
        print("você saiu do programa!")
        break
    else:
        print("erro!!! essa opção não existe; tente novamente.")