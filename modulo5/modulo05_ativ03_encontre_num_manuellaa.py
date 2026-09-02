# ==============================================================================
# 🎯 Projeto: Identificador de Maior e Menor Valor
# ==============================================================================

# 📄 Passo 1: Definir a função
# A função 'maior_menor' aceita uma lista de números como entrada.
def maior_menor(lista_numeros):
    # Verificamos se a lista está vazia
    if not lista_numeros:
        print("A lista fornecida está vazia!")
        return None, None

    # Usamos as funções nativas do Python 'max()' e 'min()'
    maior_valor = max(lista_numeros)
    menor_valor = min(lista_numeros)

    # Retornamos os dois valores encontrados
    return maior_valor, menor_valor


# ==============================================================================
# 🔹 Passo 2: Executar testes práticos

print("--- Analisando Lista de Números ---")
meus_numeros = [15, 3, 42, 8, 23, 1, 99]

# A função nos devolve dois valores ao mesmo tempo:
maior, menor = maior_menor(meus_numeros)

print(f"Lista analisada: {meus_numeros}")
print(f"Maior valor encontrado: {maior}")
print(f"Menor valor encontrado: {menor}")