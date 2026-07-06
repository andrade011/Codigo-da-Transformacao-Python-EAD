# ==============================================================================
# 1. INICIALIZAÇÃO: CADASTRO DE PRODUTOS E VARIÁVEIS DO SISTEMA
# ==============================================================================

# --- HAMBÚRGUERES ---
p1_nome = "Hamburguer de carne"
p1_estoque = 100
p1_preco = 15.90
p1_validade = "11/09/2026"
p1_descricao = "Hamburguer de carne bovina com alface, tomate e mussarela."

p2_nome = "Hamburguer de frango"
p2_estoque = 50
p2_preco = 14.90
p2_validade = "19/09/2026"
p2_descricao = "Hamburguer de frango empanado com alface, tomate e mussarela."

p3_nome = "Hamburguer vegetariano"
p3_estoque = 75
p3_preco = 17.90
p3_validade = "15/09/2026"
p3_descricao = "Hamburguer vegetariano com alface, tomate e mussarela."

# --- BEBIDAS e OUTROS ---
refri_nome = "Refrigerante 500ml"
refri_preco = 6.00

agua_nome = "Agua mineral 500ml"
agua_preco = 4.00

brownie_nome = "Brownie 300ml"
brownie_preco = 8.50

# --- VARIÁVEIS DO CARRINHO (FORA DO LOOP PRINCIPAL) ---
carrinho_nomes = []
carrinho_precos = []

# ==============================================================================
# 2. LOOP PRINCIPAL DO MENU DO SISTEMA
# ==============================================================================
while True:
    print("\n" + "-"*40)
    print("         SISTEMA HAMBURGUERIA")
    print("-"*40)
    print("1 - Para iniciar pedido (Cardápio Hamburgueres)")
    print("2 - Para ver opções de Bebidas")
    print("3 - Para ver opções de Sobremesas")
    print("4 - Para ir para a área de pagamento (Ver Carrinho)")
    print("7 - Para escolher opções de pagamento e pagar")
    print("0 - Para sair")
    print("-"*40)
    
    opcao_definida = int(input("Escolha uma opcao: "))
    
    # --- OPÇÃO 1: ADICIONAR HAMBÚRGUERES ---
    if opcao_definida == 1:
        print("\n--- Cardapio: ---")
        print(f"010- {p1_nome} (R$ {p1_preco:.2f})")
        print(f"011- {p2_nome} (R$ {p2_preco:.2f})")
        print(f"012- {p3_nome} (R$ {p3_preco:.2f})")
        print("013- hamburguer vegano (R$ 16.00)")
        print("014- batata (R$ 15.00)")
        print("015- onion rings (R$ 13.90)")
        print("016- salada (R$ 8.00)")

        codigo = input("\nDigite o código do item para adicionar ao carrinho: ")
        
        if codigo == "010":
            carrinho_nomes.append(p1_nome)
            carrinho_precos.append(p1_preco)
            print(f">> Sucesso: {p1_nome} adicionado!")
        elif codigo == "011":
            carrinho_nomes.append(p2_nome)
            carrinho_precos.append(p2_preco)
            print(f">> Sucesso: {p2_nome} adicionado!")
        
        elif codigo == "012":
            carrinho_nomes.append(p3_nome)
            carrinho_precos.append(p3_preco)
            print(f">> Sucesso: {p3_nome} adicionado!")
        
        elif codigo == "013":
            carrinho_nomes.append("hamburguer_vegano")
            carrinho_precos.append(16.00)
            print(f">> Sucesso: hamburguer_vegano adicionado!")

        elif codigo == "014":
            carrinho_nomes.append("batata")
            carrinho_precos.append(15.00)
            print(f">> Sucesso: batata adicionada!")

        elif codigo == "015":
            carrinho_nomes.append("onion_rings")
            carrinho_precos.append(13.90)
            print(f">> Sucesso: onion_rings adicionado!")

        elif codigo == "016":
            carrinho_nomes.append("sobremesa")
            carrinho_precos.append(15.00)
            print(f">> Sucesso: sobremesa adicionado!")
            
        else:
            print("[Erro] Código inválido ou item não configurado no banco de dados.")

    # --- OPÇÃO 2: ADICIONAR BEBIDAS ---
    elif opcao_definida == 2:
        print("\n--- Bebidas: ---")
        print(f"017- {refri_nome} (R$ {refri_preco:.2f})")
        print("018- Suco natural 500ml")
        print(f"019- {agua_nome} (R$ {agua_preco:.2f})")
        print("020- Cerveja litrão")
        
        codigo = input("\nDigite o código da bebida para adicionar: ")
        
        if codigo == "017":
            carrinho_nomes.append(refri_nome)
            carrinho_precos.append(refri_preco)
            print(f">> Sucesso: {refri_nome} adicionado!")
        elif codigo == "018":
            carrinho_nomes.append("suco_natural 500ml")
            carrinho_precos.append(12.00)
            print(f">> Sucesso: suco_natural adicionado!")

        elif codigo == "019":
            carrinho_nomes.append(agua_nome)
            carrinho_precos.append(agua_preco)
            print(f">> Sucesso: {agua_nome} adicionado!")

        elif codigo == "020":
            carrinho_nomes.append(cerveja_nome)
            carrinho_precos.append(cerveja_preco)
            print(f">> Sucesso: {cerveja_nome} adicionado!")

        else:
            print("[Erro] Código inválido ou bebida não configurada.")

    # --- OPÇÃO 3: ADICIONAR SOBREMESAS ---
    elif opcao_definida == 3:
        print("\n--- Sobremesas: ---")
        print("021- Milkshake 700ml")
        print(f"022- {brownie_nome} (R$ {brownie_preco:.2f})")
        print("023- Pudim 200ml")
        
        codigo = input("\nDigite o código da sobremesa para adicionar: ")
        
        if codigo == "022":
            carrinho_nomes.append(brownie_nome)
            carrinho_precos.append(brownie_preco)
            print(f">> Sucesso: {brownie_nome} adicionado!")
        else:
            print("[Erro] Código inválido ou sobremesa não configurada.")

    # --- OPÇÃO 4: RESUMO DO PEDIDO / CARRINHO ---
    elif opcao_definida == 4:
        print("\n=== SEU CARRINHO ATUAL ===")
        if not carrinho_nomes:
            print("Seu carrinho está vazio!")
        else:
            for i in range(len(carrinho_nomes)):
                print(f"- {carrinho_nomes[i]}: R$ {carrinho_precos[i]:.2f}")
            print("-"*25)
            total_atual = sum(carrinho_precos)
            print(f"Total Acumulado: R$ {total_atual:.2f}")

    # --- OPÇÃO 7: ESCOLHER OPÇÃO DE PAGAMENTO E FINALIZAR ---
    elif opcao_definida == 7:
        if not carrinho_nomes:
            print("\n[Aviso] O carrinho está vazio. Adicione itens antes de pagar!")
        else:
            total_final = sum(carrinho_precos)
            print(f"\nTotal da Conta: R$ {total_final:.2f}")
            print("Formas de Pagamento disponíveis:")
            print("1- Cartão de Crédito / Débito")
            print("2- PIX")
            
            forma_pagamento = input("Escolha a forma de pagamento (1 ou 2): ")
            
            if forma_pagamento in ["1", "2"]:
                print("\nProcessando e validando pagamento...")
                print("PAGAMENTO REALIZADO COM SUCESSO! 🍔")
                print("Pedido enviado para a produção na cozinha.")
                
                # Importante: Limpa o carrinho para o próximo cliente entrar
                carrinho_nomes.clear()
                carrinho_precos.clear()
            else:
                print("[Erro] Opção de pagamento inválida. Tente novamente.")

    # --- OPÇÃO 0: SAIR DO SISTEMA ---
    elif opcao_definida == 0:
        print("\nSaindo do sistema da Hamburgueria... Até breve!")
        break
        
    else:
        print("[Erro] Opção inválida no Menu Principal!")