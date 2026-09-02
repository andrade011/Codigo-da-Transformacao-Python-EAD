import csv

nome_arquivo = "notas_alunos.csv"

# --- 1. Adicionar / Salvar notas em CSV ---
alunos_notas = [
    ["Nome", "Nota1", "Nota2", "Media"],
    ["Ivan Silva", 8.5, 7.0, 7.75],
    ["Beatriz Vitoria", 9.0, 9.5, 9.25],
    ["Eric Renan", 6.0, 5.5, 5.75]
]

# Escrevendo no arquivo CSV
with open(nome_arquivo, mode="w", newline="", encoding="utf-8") as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerows(alunos_notas)

print(f"📊 Dados de notas salvos em '{nome_arquivo}' com sucesso!")

# --- 2. Carregar e exibir informações do CSV ---
print("\n--- 📖 Lendo e exibindo notas do arquivo CSV ---")
with open(nome_arquivo, mode="r", encoding="utf-8") as arquivo:
    leitor = csv.reader(arquivo)
    for linha in leitor:
        print(f"Aluno: {linha[0]:<15} | Nota 1: {linha[1]:<5} | Nota 2: {linha[2]:<5} | Média: {linha[3]}")