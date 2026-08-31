agenda = {}

while True:
    print("\n--- AGENDA DE CONTATOS ---")
    print("1. Adicionar/Atualizar | 2. Remover | 3. Buscar | 4. Sair")
    opcao = input("Opção: ")

    if opcao == "1":
        nome = input("Nome: ").strip()
        telefone = input("Telefone: ").strip()
        agenda[nome] = telefone
        print("Contato salvo com sucesso!")
    elif opcao == "2":
        nome = input("Nome do contato a remover: ").strip()
        if nome in agenda:
            del agenda[nome]
            print(f"{nome} foi removido.")
        else:
            print("Contato não encontrado.")
    elif opcao == "3":
        nome = input("Nome do contato a buscar: ").strip()
        if nome in agenda:
            print(f"Telefone de {nome}: {agenda[nome]}")
        else:
            print("Contato não encontrado.")
    elif opcao == "4":
        print("Encerrando a agenda...")
        break
    else:
        print("Opção inválida!")