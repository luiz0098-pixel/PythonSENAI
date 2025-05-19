# exemplo dicionario
# dicionario usa {}

# criar
aluno = {
    "nome": "luiz",
    "idade": 16,
    "altura": 1.80,
    "matriculado": True 
}

# primeiro filme
filmeum = {
    "nome":"Como Eu Era Antes de Você",
    "lancamento": "16 de junho de 2016",
    "diretor":"Thea Sharrock"
}
# segundo filme 
filmedois = {
    "nome":"O Macaco",
    "lancamento":"20 de fevereiro de 2025 ",
    "diretor":"Oz Perkins" 
 }
# terceiro filme 
filmetres = {
    "nome":"Invocação do Mal",
    "lancamento":"13 de setembro de 2013",
    "diretor":"James Wan"    
}
# print(aluno)

# adicionar campo
aluno["peso"] = 85

#print(aluno)

# alterar campo
aluno["idade"]= 17
#print(aluno)

#deletar campo
del aluno["altura"]
#print(aluno)

# verificar
if "altura" in aluno:
    print("altura existente")
else:
    print("altura inexistente")
    
# exibir
for chave, valor in aluno.items():
    print(f"{chave }: {valor}")
print("")

    
#exibir uma lista de dicionarios
lista_filme = [filmeum, filmedois,filmetres]
    #escolhendo os campos
for filme in lista_filme:
    print(f"{filme['diretor']}")
    
    #exibindo todos
for filme in lista_filme:
    for chave, valor in filme.items():
          print(f"{chave }: {valor}")
    print("")
        
        