print("sistema de cadastro para biblioteca escolar")

def cadastrar_livro():
    isbn = input("digite o ISBN do livro (único): ")
    
    titulo = input("digite o título do livro: ")
    autor = input("digite o autor do livro: ")
    categoria = input("digite a categoria do livro: ")
    ano_publicacao = input("digite o ano de publicação do livro: ")
    return {
        "isbn": isbn,
        "titulo": titulo,
        "autor": autor,
        "categoria": categoria,
        "ano_publicacao": ano_publicacao,
    }

def exibir_livros(livros):
    if not livros:
        print("nenhum livro cadastrado.")
        return
    print("lista de todos os livros cadastrados:")
    for livro in livros:
        print(f"ISBN: {livro['isbn']}")
        print(f"titulo: {livro['titulo']}")
        print(f"autor: {livro['autor']}")
        print(f"categoria: {livro['categoria']}")
        print(f"ano de publicação: {livro['ano_publicacao']}")
        print("")

def criar_lista_titulos(livros):
    if not livros:
        print("nenhuma lista de títulos para gerar.")
        return
    print("lista de titulos para etiquetagem:")
    for livro in livros:
        print(livro["titulo"])

def buscar_livro_por_isbn(livros):
    isbn = input("digite o ISBN do livro que deseja buscar: ")
    for livro in livros:
        if livro['isbn'] == isbn:
            print("Livro encontrado:")
            print(f"ISBN: {livro['isbn']}")
            print(f"titulo: {livro['titulo']}")
            print(f"autor: {livro['autor']}")
            print(f"categoria: {livro['categoria']}")
            print(f"ano de publicação: {livro['ano_publicacao']}")
            return
    print("Livro não encontrado.")

def buscar_livros_por_autor(livros):
    autor = input("digite o nome do autor que deseja buscar: ")
    encontrados = [livro for livro in livros if livro['autor'] == autor]
    if not encontrados:
        print("nenhum livro foi encontrado no nome desse autor.")
        return
    print(f"livros encontrados no nome do autor {autor}:")
    for livro in encontrados:
        print(f"ISBN: {livro['isbn']}, Título: {livro['titulo']}")

def buscar_livros_por_categoria(livros):
    categoria = input("digite a categoria que deseja buscar: ")
    encontrados = [livro for livro in livros if livro['categoria'] == categoria]
    if not encontrados:
        print("nenhum livro encontrado nessa categoria.")
        return
    print(f"livros encontrados na categoria {categoria}:")
    for livro in encontrados:
        print(f"ISBN: {livro['isbn']}, titulo: {livro['titulo']}")

def editar_livro(livros):
    isbn = input("digite o ISBN do livro que deseja editar: ")
    for livro in livros:
        if livro['isbn'] == isbn:
            print("livro encontrado. Insira os novos dados! caso queira mudar somente algumas informaçoes,")
            print("coloque a mesma informação que estava.")
            print("")
            
            novo_titulo = input(f"titulo atual: {livro['titulo']} - novo titulo: ")
            novo_autor = input(f"autor atual: {livro['autor']} - novo autor: ")
            nova_categoria = input(f"categoria atual: {livro['categoria']} - nova categoria: ")
            novo_ano = input(f"ano de publicação atual: {livro['ano_publicacao']} - novo ano: ")

            if novo_titulo:
                livro['titulo'] = novo_titulo
            if novo_autor:
                livro['autor'] = novo_autor
            if nova_categoria:
                livro['categoria'] = nova_categoria
            if novo_ano:
                livro['ano_publicacao'] = novo_ano

            print("os dados do livro foi atualizado com sucesso!!")
            return
    print("livro não encontrado.")

livros = []
while True:
    print("menu:")
    print("1- cadastrar livro")
    print("2- exibir livros")
    print("3- gerar lista de titulos")
    print("4- buscar livro por ISBN")
    print("5- buscar livros por autor")
    print("6- buscar livros pela categoria")
    print("7- editar um livro")
    print("8- sair")
    
    opcao = input("Escolha uma opção: ")
    print("")

    if opcao == "1":
        novo_livro = cadastrar_livro()
        livros.append(novo_livro)
        print("livro cadastrado com sucesso!")
        print("")
    elif opcao == "2":
        exibir_livros(livros)
        print("")
    elif opcao == "3":
        criar_lista_titulos(livros)
        print("")
    elif opcao == "4":
        buscar_livro_por_isbn(livros)
        print("")
    elif opcao == "5":
        buscar_livros_por_autor(livros)
        print("")
    elif opcao == "6":
        buscar_livros_por_categoria(livros)
        print("")
    elif opcao == "7":
        editar_livro(livros)
        print("")
    elif opcao == "8":
        print("você saiu!")
        break
    else:
        print("erro!!! essa opção não existe; tente novamente.")

print(f"livros cadastrados no total: {len(livros)}")