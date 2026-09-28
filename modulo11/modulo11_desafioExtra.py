import sqlite3

# Conexão com o banco de dados
conexao = sqlite3.connect('modulo11.db')
cursor = conexao.cursor()

# ==============================================================================
# DESAFIO EXTRA: Criação da Tabela e Funções de Tarefas
# ==============================================================================
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Tarefas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        descricao TEXT NOT NULL
    )
''')
conexao.commit()

def adicionar_tarefa(descricao):
    """Adiciona uma nova tarefa"""
    cursor.execute("INSERT INTO Tarefas (descricao) VALUES (?)", (descricao,))
    conexao.commit()
    print(f"Tarefa '{descricao}' adicionada com sucesso!")

def listar_tarefas():
    """Visualiza todas as tarefas"""
    cursor.execute("SELECT * FROM Tarefas")
    tarefas = cursor.fetchall()
    print("\n--- Gerenciador de Tarefas ---")
    for t in tarefas:
        print(f"ID: {t[0]} | Descrição: {t[1]}")

def excluir_tarefa(id_tarefa):
    """Exclui uma tarefa pelo ID"""
    cursor.execute("DELETE FROM Tarefas WHERE id = ?", (id_tarefa,))
    conexao.commit()
    print(f"Tarefa ID {id_tarefa} excluída com sucesso!")


# ==============================================================================
# EXECUÇÃO E TESTES DO DESAFIO
# ==============================================================================
if __name__ == '__main__':
    print("=== EXECUTANDO DESAFIO EXTRA ===")
    
    adicionar_tarefa("Estudar Python no Visual Studio Code")
    adicionar_tarefa("Enviar arquivos para a pasta Modulo_11 no GitHub")
    
    listar_tarefas()
    
    excluir_tarefa(1)
    
    listar_tarefas()

    # Fechando conexão
    conexao.close()