import sqlite3

# Conexão com o banco de dados
conexao = sqlite3.connect('modulo11.db')
cursor = conexao.cursor()

# ==============================================================================
# ATIVIDADE 1: Criação da Tabela 'Clientes'
# ==============================================================================
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL
    )
''')
conexao.commit()


# ==============================================================================
# ATIVIDADE 2: Operações CRUD
# ==============================================================================
def inserir_cliente(nome, email):
    """C - Create (Inserir)"""
    cursor.execute("INSERT INTO Clientes (nome, email) VALUES (?, ?)", (nome, email))
    conexao.commit()
    print(f"Cliente '{nome}' cadastrado com sucesso!")

def listar_clientes():
    """R - Read (Consultar)"""
    cursor.execute("SELECT * FROM Clientes")
    clientes = cursor.fetchall()
    print("\n--- Lista de Clientes ---")
    for c in clientes:
        print(f"ID: {c[0]} | Nome: {c[1]} | Email: {c[2]}")

def atualizar_email(id_cliente, novo_email):
    """U - Update (Atualizar)"""
    cursor.execute("UPDATE Clientes SET email = ? WHERE id = ?", (novo_email, id_cliente))
    conexao.commit()
    print(f"Email do ID {id_cliente} atualizado com sucesso!")

def deletar_cliente(id_cliente):
    """D - Delete (Deletar)"""
    cursor.execute("DELETE FROM Clientes WHERE id = ?", (id_cliente,))
    conexao.commit()
    print(f"Cliente ID {id_cliente} removido com sucesso!")


# ==============================================================================
# ATIVIDADE 3: Consultas de Filtro SQL
# ==============================================================================
def buscar_clientes_por_letra(letra_inicial):
    cursor.execute("SELECT * FROM Clientes WHERE nome LIKE ?", (letra_inicial + '%',))
    resultados = cursor.fetchall()
    print(f"\n--- Clientes começando com '{letra_inicial}' ---")
    for c in resultados:
        print(f"ID: {c[0]} | Nome: {c[1]} | Email: {c[2]}")


# ==============================================================================
# EXECUÇÃO E TESTES
# ==============================================================================
if __name__ == '__main__':
    print("=== EXECUTANDO ATIVIDADES 1, 2 E 3 ===")
    
    # Inserindo clientes
    inserir_cliente("Ana Silva", "ana@email.com")
    inserir_cliente("Arthur Souza", "arthur@email.com")
    inserir_cliente("Carlos Lima", "carlos@email.com")

    # Listando todos
    listar_clientes()

    # Atualizando e deletando
    atualizar_email(1, "ana.silva@novoemail.com")
    deletar_cliente(3)

    # Filtrando por letra inicial
    buscar_clientes_por_letra("A")

    # Fechando conexão
    conexao.close()