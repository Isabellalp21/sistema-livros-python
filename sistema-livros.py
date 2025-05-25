livros = []

def adicionar_livro():
    titulo = input("Título: ")
    autor = input("Autor: ")
    ano = input("Ano de publicação: ")
    livros.append({"titulo": titulo, "autor": autor, "ano": ano})
    print("📚 Livro adicionado com sucesso!")

def listar_livros():
    if not livros:
        print("Nenhum livro cadastrado.")
        return
    for i, livro in enumerate(livros):
        print(f"{i+1}. {livro['titulo']} - {livro['autor']} ({livro['ano']})")

def buscar_livro():
    termo = input("Digite o título a buscar: ").lower()
    encontrados = [l for l in livros if termo in l['titulo'].lower()]
    if encontrados:
        for livro in encontrados:
            print(f"📖 {livro['titulo']} - {livro['autor']} ({livro['ano']})")
    else:
        print("🔍 Nenhum livro encontrado com esse título.")

def remover_livro():
    listar_livros()
    try:
        indice = int(input("Número do livro a remover: ")) - 1
        if 0 <= indice < len(livros):
            removido = livros.pop(indice)
            print(f"❌ Livro '{removido['titulo']}' removido.")
        else:
            print("Número inválido.")
    except:
        print("Erro ao tentar remover o livro.")

while True:
    print("\n📚 MENU")
    print("1 - Adicionar livro")
    print("2 - Listar livros")
    print("3 - Buscar livro")
    print("4 - Remover livro")
    print("5 - Sair")

    escolha = input("Escolha uma opção: ")
    if escolha == "1":
        adicionar_livro()
    elif escolha == "2":
        listar_livros()
    elif escolha == "3":
        buscar_livro()
    elif escolha == "4":
        remover_livro()
    elif escolha == "5":
        print("Saindo... Até mais!")
        break
    else:
        print("Opção inválida.")
