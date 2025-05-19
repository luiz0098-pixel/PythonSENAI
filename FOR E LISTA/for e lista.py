objetos = ["mesa", "cadeira", "borracha", "lapis", "garrafa"]
print("lista criada")

objetos.append("caderno")
print("objeto adicionado")

print(objetos[1])
print("objeto na segunda posição acessado")

removidos = objetos.pop(2)
print(removidos)
print("objetos removidos")

print(len(objetos))
print("tamanho da lista exibido")

for objeto in objetos:
    print(objeto)
    
    if "cadeira" in objetos:
        objetos.remove("cadeira")
        print("cadeira removida")
    else :
        objetos.append("cadeira")
        print("cadeira adicionada")
        
    print(objetos)
    objetos.sort()
    print("lista organizada em ordem alfabetica")
    
    print(objetos)
    objetos.append(0)
    print("primeiro objeto exibido")
    
    ultimo = objetos.pop()
    objetos.append(ultimo)
    print(ultimo)
    print("ultimo objeto exibido")
    
    objetos.clear()
    print("lista limpa")