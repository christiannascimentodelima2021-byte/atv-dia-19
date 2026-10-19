#======================================================================================#
#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\//\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/#
#Parte 2 da tarefa
#2/2!!


materiais = {
    "mouse": 10,
    "teclado": 6,
    "cabo": 20
}

nome = input("Qual material deseja retirar? ").strip().lower()

# 1. Verificar se o material existe no dicionário
if nome not in materiais:
    print("Erro: Material não encontrado no estoque!")
else:
    try:
        quantidade = int(input("Quantas unidades? "))
        
        # 2. Impedir quantidades iguais ou menores que zero
        if quantidade <= 0:
            print("Erro: A quantidade a ser retirada deve ser maior que zero!")
            
        # 3. Impedir a retirada de mais unidades do que existem
        elif quantidade > materiais[nome]:
            print(f"Erro: Estoque insuficiente! Existem apenas {materiais[nome]} unidades de '{nome}'.")
            
        else:
            # 4. Atualizar o estoque quando a operação for válida
            materiais[nome] = materiais[nome] - quantidade
            print("Retirada realizada com sucesso!")
            
            # 5. Exibir o estoque atualizado
            print("\n--- ESTOQUE ATUALIZADO ---")
            for item, qtd in materiais.items():
                print(f"- {item.capitalize()}: {qtd} unidades")
                
    except ValueError:
        print("Digite uma quantidade numérica válida!")