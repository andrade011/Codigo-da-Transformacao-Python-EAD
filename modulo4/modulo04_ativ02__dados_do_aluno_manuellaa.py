aluno = {
    "nome": "Lucas",
    "idade": 17,
    "notas": [8.5, 9.0, 7.5]
}

print("--- Dados do Aluno ---")
print(f"Nome: {aluno['nome']}")
print(f"Idade: {aluno['idade']} anos")
print(f"Notas: {aluno['notas']}")
print(f"Média: {sum(aluno['notas']) / len(aluno['notas']):.2f}")