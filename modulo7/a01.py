from datetime import datetime, timedelta, timezone
import random

# 1. Listas para simular nomes aleatórios em português
nomes = ["Ana", "Bruno", "Carlos", "Diana", "Eduardo", "Fernanda", "Gabriel", "Juliana"]
sobrenomes = ["Silva", "Santos", "Oliveira", "Souza", "Rodrigues", "Almeida", "Lima"]

# Gera um nome completo aleatório
cliente_aleatorio = f"{random.choice(nomes)} {random.choice(sobrenomes)}"

# 2. Gera uma data aleatória nos últimos 365 dias
dias_aleatorios = random.randint(0, 365)
segundos_aleatorios = random.randint(0, 86400) # Segundos em um dia

# Subtrai o tempo aleatório da data e hora atuais
agora = datetime.now(timezone.utc)
data_registro = agora - timedelta(days=dias_aleatorios, seconds=segundos_aleatorios)

# 3. Calcula o vencimento (prazo de 30 dias)
data_vencimento = data_registro + timedelta(days=30)

# Exibe os resultados formatados
print(f"Cliente: {cliente_aleatorio}")
print(f"Data do Registro: {data_registro.strftime('%d/%m/%Y %H:%M:%S')}")
print(f"Data de Vencimento: {data_vencimento.strftime('%d/%m/%Y')}")
