#======================================================================================#
#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\//\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/#
#Parte 1 da tarefa
#1/2!!
estoque = [
    {"codigo": 101, "nome": "Teclado", "quantidade": 8, "preco": 75.0},
    {"codigo": 102, "nome": "Mouse", "quantidade": 15, "preco": 40.0},
    {"codigo": 103, "nome": "Monitor", "quantidade": 4, "preco": 850.0}
]

def cadastrar_produto():
    print("\n--- CADASTRAR PRODUTO ---")
    try:
        codigo = int(input("Código do produto: "))
    except ValueError:
        print("O código deve ser um número inteiro!")
        return

    for p in estoque:
        if p["codigo"] == codigo:
            print("Esse código já existe!")
            return

    nome = input("Nome do produto: ").strip()
    try:
        quantidade = int(input("Quantidade inicial: "))
        preco = float(input("Preço unitário: "))
    except ValueError:
        print("Digite valores numéricos válidos!")
        return

    produto = {
        "codigo": codigo,
        "nome": nome,
        "quantidade": quantidade,
        "preco": preco
    }
    estoque.append(produto)
    print("Produto cadastrado com sucesso!")

def listar_produtos():
    print("\n--- PRODUTOS CADASTRADOS ---")
    if len(estoque) == 0:
        print("Nenhum produto cadastrado.")
        return
    for produto in estoque:
        print(
            f"Código: {produto['codigo']} | "
            f"Nome: {produto['nome']} | "
            f"Quantidade: {produto['quantidade']} | "
            f"Preço: R$ {produto['preco']:.2f}"
        )

def pesquisar_produto():
    print("\n--- PESQUISAR PRODUTO ---")
    try:
        codigo = int(input("Digite o código: "))
    except ValueError:
        print("O código precisa ser um número inteiro!")
        return
    
    encontrado = False
    for produto in estoque:
        if produto["codigo"] == codigo:
            print("\nProduto encontrado:")
            print(f"Nome: {produto['nome']}")
            print(f"Quantidade: {produto['quantidade']}")
            print(f"Preço: R$ {produto['preco']:.2f}")
            encontrado = True
            break
            
    if not encontrado:
        print("Produto não encontrado!")

def registrar_entrada():
    print("\n--- ENTRADA DE MERCADORIA ---")
    try:
        codigo = int(input("Código do produto: "))
    except ValueError:
        print("Código inválido!")
        return

    encontrado = False
    for produto in estoque:
        if produto["codigo"] == codigo:
            encontrado = True
            try:
                quantidade = int(input("Quantidade recebida: "))
                if quantidade < 0:
                    print("A quantidade não pode ser negativa!")
                    return
            except ValueError:
                print("A quantidade deve ser um número inteiro!")
                return
            
            produto["quantidade"] += quantidade
            print("Entrada registrada com sucesso!")
            break

    if not encontrado:
        print("Produto não encontrado!")

def menu():
    while True:
        print("\n==============================")
        print("       SISTEMA DE ESTOQUE     ")
        print("==============================")
        print("1. Cadastrar produto")
        print("2. Listar produtos")
        print("3. Pesquisar produto")
        print("4. Registrar entrada")
        print("5. Sair")
        
        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Por favor, digite um número válido!")
            continue
            
        if opcao == 1:
            cadastrar_produto()
        elif opcao == 2:
            listar_produtos()
        elif opcao == 3:
            pesquisar_produto()
        elif opcao == 4:
            registrar_entrada()
        elif opcao == 5:
            print("Saindo do sistema... Até logo!")
            break
        else:
            print("Opção inválida! Escolha entre 1 e 5.")

if __name__ == "__main__":
    menu()