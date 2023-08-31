# Criação de uma lista para armazenar os produtos
produtos = []

# Função para cadastrar um novo produto
def cadastrar_produto():
    print("Cadastro de Produto")
    codigo = input("Digite o código do produto: ")
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    produtos.append({"Código": codigo, "Nome": nome, "Preço": preco})
    print("Produto cadastrado com sucesso!")

# Função para listar todos os produtos cadastrados
def listar_produtos():
    print("Lista de Produtos:")
    for produto in produtos:
        print(f"Código: {produto['Código']}, Nome: {produto['Nome']}, Preço: R${produto['Preço']:.2f}")

# Função principal
def main():
    while True:
        print("\n1 - Cadastrar produto")
        print("2 - Listar produtos")
        print("3 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_produto()
        elif opcao == "2":
            listar_produtos()
        elif opcao == "3":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")


main()