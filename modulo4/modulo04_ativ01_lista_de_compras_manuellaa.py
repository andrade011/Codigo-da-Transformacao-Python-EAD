lista_compras = []

while True:
    print(f"\nLista atual: {lista_compras}")
    print("1. Adicionar item | 2. Remover item | 3. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        item = input("Digite o item para adicionar: ")
        lista_compras.append(item)
        print(f"'{item}' adicionado!")
    elif opcao == "2":
        item = input("Digite o item para remover: ")
        if item in lista_compras:
            lista_compras.remove(item)
            print(f"'{item}' removido!")
        else:
            print("Item não encontrado.")
    elif opcao == "3":
        print("Saindo da lista de compras...")
        break
    else:
        print("Opção inválida!")